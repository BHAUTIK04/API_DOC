from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list', views.list),
    url(r'^detail', views.detail),
    url(r'^create', views.createNew),
]
