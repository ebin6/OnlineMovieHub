from django.shortcuts import render,redirect
from actors.forms import ActorForm
from django.contrib import messages


# Create your views here.

def addActor(request):
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
    return render(request,'actors/add-actor.html',{"my_form":form_obj})