# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:38:02 2017

@author: alesha
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<name>\w+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<name>\w+)/$', views.edit, name='edit'),
    url(r'^message/(?P<name>\w+)/$', views.message, name='message')
]