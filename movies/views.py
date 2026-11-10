from django.shortcuts import render,redirect
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
        movie=request.POST.get('movie')
        re_date=request.POST.get('release_date')
        cate=request.POST.get('category')
        description=request.POST.get('desc')
        poster=request.FILES.get('poster')
        rating=request.POST.get('rating')
        category=Category.objects.get(id=cate)
        Movie(name=movie,description=description,release_date=re_date,
              rating=rating,poster=poster,category=category).save()
        return redirect("all_movies")
    return render(request,"add-movie.html",{"all_categories":categories})

def movieDetail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"movie-detail.html",{"movie":movie})

def updateMovie(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    categories=Category.objects.all()

    return render(request,"update-movie.html",{"movie":movie,"all_categories":categories})
