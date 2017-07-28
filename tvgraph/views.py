# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import imdb

def index(request):
#==============================================================================
    return render(request, "tvgraph/index.html")
    #return HttpResponse("What's up, world. You're at the tvgraph index which has not been made yet because I don't know how to continue. So you'll just have to wait for now. Sorry. See ya later, world.")
#==============================================================================

def find(request):
    #return HttpResponse(request.POST["movie"])
    name = request.POST["movie"]
    i = imdb.IMDb()
    movie = i.search_movie(name)[0]
    ratings = i.get_movie_episodes_rating(movie.getID())
    episodes = ratings["data"]["episodes rating"]
    #for episode in episodes:
    #   print episode["rating"]
    context = {"episodes" : episodes}
    return render(request, 'tvgraph/details.html', context)


def detail(request, name):
    # request imdb ratings for name
    # return imdb ratings for that name
    
    i = imdb.IMDb()
    movie = i.search_movie(name)[0]
    ratings = i.get_movie_episodes_rating(movie.getID())
    episodes = ratings["data"]["episodes rating"]
    #for episode in episodes:
    #   print episode["rating"]
    context = {"episodes" : episodes}
    return render(request, 'tvgraph/details.html', context)
    
    #return HttpResponse("You are searching for the show named " + name + ".")
def edit(request, name):
     return HttpResponse("You are now editing " + name + ".")
def message(request, name):
    return HttpResponse("You are now reading a message from " + name + ". ") 