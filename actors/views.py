from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from actors.forms import ActorForm
from django.contrib import messages
from actors.models import Actors

from django.views.generic import CreateView,ListView,DetailView


# Create your views here.

'''def addActor(request):
    if request.method=="POST":
        form_obj=ActorForm(request.POST,request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("movies:index")
        else:
            messages.info(request,"Invalid details")
            return redirect("actors:add_actors")
    else:
        form_obj=ActorForm()
    return render(request,'actors/add-actor.html',{"my_form":form_obj})'''

class AddActor(CreateView):
    model=Actors
    form_class=ActorForm
    template_name="actors/add-actor.html"
    success_url=reverse_lazy("movies:index")


class ListActors(ListView):
    model=Actors
    template_name="actors/all-actors.html"
    context_object_name="actors"


class ActorDetail(DetailView):
    model=Actors
    template_name="actors/actor-detail.html"
    context_object_name="actor"