from django.shortcuts import render

# Create your views here.

def addActor(request):
    return render(request,'actors/add-actor.html')