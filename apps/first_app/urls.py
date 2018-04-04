from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login, name='do_the_login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^friends$', views.friends),
    url(r'^user/(?P<id>\d+)$', views.show),
    url(r'^user/add/(?P<id>\d+)$', views.add_friend),
    url(r'^user/delete/(?P<id>\d+)$', views.delete_friend),
]