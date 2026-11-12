from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def signUp(request):
    if request.method=="POST":
        first_name=request.POST.get("f_name")
        last_name=request.POST.get("l_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if User.objects.filter(username=email).exists():
            return HttpResponse("Username already exists")
        else:
            User.objects.create_user(username=email,first_name=first_name,last_name=last_name,password=password).save()
            return redirect("login")
    return render(request,"register.html")


def signIn(request):
    return render(request,"login.html")