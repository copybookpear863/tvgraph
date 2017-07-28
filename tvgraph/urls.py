# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:38:02 2017

@author: alesha
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<name>.*)/$', views.detail, name='detail'),
    url(r'^find/$', views.find, name='find'),
    url(r'^message/(?P<name>\w+)/$', views.message, name='message')
]