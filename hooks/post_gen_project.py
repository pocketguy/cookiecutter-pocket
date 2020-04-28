#!/usr/bin/env python

import subprocess

author_name = "{{cookiecutter.author_name}}"
author_email = "{{cookiecutter.author_email}}"

subprocess.call(["git", "init"])
subprocess.call(["git", "config", "user.name", author_name])
subprocess.call(["git", "config", "user.email", author_email])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])
