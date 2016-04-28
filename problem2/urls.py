"""Urls of problem2 app."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display, name='problem2_display'),
]
