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
     return HttpResponse("You are now reading a message from " + name + ". If you are reading this, it's too late for me, and I suggest you save yourselves. I don't know how you will do this, but just please be aware that THE AIR IS CRACK and that may ormay not help you depending on the purpose of your trip. I wish you a successful escape from the lair of the crack doers and I hope nobody on the internet can read or interpret this message. Adios my friend. btw this was meant for my good friends Esperanza Michala and DHMI Gisselle so if you accidentally stumbled upon this don't even try to understand what I mean. Thanks,and best of luck to you. Choose your crack wisely.")