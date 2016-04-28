from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.display, name='problem2_display'),
]
