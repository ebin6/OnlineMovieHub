from django.db import models

# Create your models here.
class Actors(models.Model):
    name=models.CharField(max_length=70)
    dob=models.DateField()
    about=models.TextField()
    image=models.ImageField(upload_to="actors/")
    