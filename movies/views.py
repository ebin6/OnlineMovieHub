from django.shortcuts import render
from movies.models import Movie,Category
# Create your views here.

def home(request):
    return render(request,"index.html")

def allMovies(request):
    movies=Movie.objects.all()
    return render(request,"all-movies.html",{"all_movies":movies})

def addMovie(request):
    categories=Category.objects.all()
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
    return render(request,"add-movie.html",{"all_categories":categories})