from django.contrib import admin
from movies.models import Movie,Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)

