from django.urls import path
from movies import views

urlpatterns=[
    path("",views.home,name="index"),
    path("all-movies/",views.allMovies,name="all_movies"),
    path("add-movie/",views.addMovie,name="add_movie"),
    path("movie-detail/<int:movie_id>",views.movieDetail,name="movie_detail"),
    path("movie-update/<int:movie_id>",views.updateMovie,name="edit_movie"),
    path("delete-movie/<int:movie_id>",views.deleteMovie,name="delete_movie"),
]


