from django.shortcuts import render
from actors.forms import ActorForm

# Create your views here.

def addActor(request):
    form_obj=ActorForm()
    return render(request,'actors/add-actor.html',{"my_form":form_obj})