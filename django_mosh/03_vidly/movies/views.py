from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies

# Create your views here.
def  index(request) :
    movies = Movies.objects.all();
    movie_names = ', '.join([m.title for m in movies])
    return HttpResponse(movie_names);