# coding: utf-8
from __future__ import absolute_import

# Standard imports
import os

# External imports
from django.core.wsgi import get_wsgi_application


# Set environment variable `DJANGO_SETTINGS_MODULE` default value
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aoikdjangostudy.settings")

# Get WSGI application
application = get_wsgi_application()
