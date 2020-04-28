#!/bin/bash

set -eu

rm -f db.sqlite3
find . -wholename '*/migrations/0*' -delete
./manage.py makemigrations
./manage.py migrate

echo "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'password')
" | python manage.py shell
