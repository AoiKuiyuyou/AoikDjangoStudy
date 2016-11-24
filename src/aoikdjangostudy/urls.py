# coding: utf-8
from __future__ import absolute_import

# External imports
from aoikdjangostudy.views import CustomRequestHandler
from django.conf.urls import url


# URL-to-handler mappings
urlpatterns = [
    url(r'^', CustomRequestHandler),
]
