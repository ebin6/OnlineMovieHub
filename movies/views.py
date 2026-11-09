from django.shortcuts import render
from movies.models import Movie
# Create your views here.

def home(request):
    return render(request,"index.html")

def allMovies(request):
    movies=Movie.objects.all()
    return render(request,"all-movies.html",{"all_movies":movies})