from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns, include, url

from . import autodiscover
from .views import home

autodiscover()

urlpatterns = [
    url(r'^$', home, name='health_check_home'),
]
