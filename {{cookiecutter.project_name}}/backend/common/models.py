from uuid import uuid4

from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class SystemManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(Q(deleted_at__isnull=True) | Q(deleted_at__gt=timezone.now()))
        )


class SystemModel(models.Model):
    objects_unsafe = models.Manager()
    objects = SystemManager()

    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(_("creation date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update date"), auto_now=True)
    deleted_at = models.DateTimeField(_("deletion date"), null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self, *args, **kwargs):
        self.deleted_at = None
        self.save()

    @property
    def is_deleted(self):
        return self.deleted_at is not None and self.deleted_at < timezone.now()
