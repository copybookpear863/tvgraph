# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tvgraph index.")

def detail(request, name):
    # request imdb ratings for name
    # return imdb ratings for that name
    return HttpResponse("You are searching for the show named " + name + ".")
def edit(request, name):
     return HttpResponse("You are now editing " + name + ".")
def message(request, name):
     return HttpResponse("You are now reading a message from " + name + ".")