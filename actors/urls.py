from django.urls import path

from actors import views

app_name="actors"

urlpatterns=[
    # path("add-actor/",views.addActor,name="add_actors")
    path("add-actor/",views.AddActor.as_view(),name="add_actors")
]