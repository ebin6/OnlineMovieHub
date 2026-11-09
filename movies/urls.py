from django.urls import path
from movies import views

urlpatterns=[
    path("",views.home,name="index"),
    path("all-movies/",views.allMovies,name="all_movies"),
    path("add-movie/",views.addMovie,name="add_movie")
]


