from django.contrib import admin
from movies.models import Movie,Category

# Register your models here.

admin.site.register(Movie)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":["category"]}

admin.site.register(Category,CategoryAdmin)