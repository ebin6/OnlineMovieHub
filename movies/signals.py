from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from movies.models import Movie

@receiver(post_delete,sender=Movie)
def delete_poster(sender,instance,**kwargs):
    if instance.poster:
        image_path=instance.poster.name

        if image_path!="posters/movie_default_poster.jpg":
            if default_storage.exists(image_path):
                default_storage.delete(image_path)