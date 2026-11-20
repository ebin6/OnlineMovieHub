from django.urls import path

from actors import views

app_name="actors"

urlpatterns=[
    # path("add-actor/",views.addActor,name="add_actors")
    path("add-actor/",views.AddActor.as_view(),name="add_actors"),
    path("list-actors/",views.ListActors.as_view(),name="list_actors"),
    path("actor-detail/<int:pk>",views.ActorDetail.as_view(),name="actor_detail"),
    path("update-actor/<int:pk>",views.UpdateActor.as_view(),name="update_actor")
]