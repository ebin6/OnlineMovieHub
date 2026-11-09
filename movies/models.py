from django.db import models

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Movie(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    release_date=models.DateField()
    rating=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    poster=models.ImageField(upload_to="posters/",default="posters/movie_default_poster.jpg")

    def __str__(self):
        return self.name
