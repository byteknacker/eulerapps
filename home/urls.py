from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.display, name='home_display'),
]
