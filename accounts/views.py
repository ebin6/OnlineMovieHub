from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
from accounts.models import Profile

# Create your views here.

def signUp(request):
    if request.method=="POST":
        first_name=request.POST.get("f_name")
        last_name=request.POST.get("l_name")
        email=request.POST.get("email")
        password=request.POST.get("password")

        phone=request.POST.get("phone")
        if User.objects.filter(username=email).exists():
            messages.info(request,"Username already exists")
            return redirect("accounts:register")
        else:
            user=User.objects.create_user(username=email,first_name=first_name,
                                     last_name=last_name,password=password)
            profile=Profile(user=user,phone=phone)
            if "profile_pic" in request.FILES:
                profile_pic=request.FILES("profile_pic")
                profile.profile_pic=profile_pic
            profile.save()
            messages.success(request,"Registration completed . Please login to continue")
            return redirect("accounts:login")
    return render(request,"register.html")


def signIn(request):
    if request.method=="POST":
        username=request.POST.get("username")
        passwd=request.POST.get("passwd")
        user=auth.authenticate(username=username,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("movies:index")
        else:
            messages.error(request,"Invalid username or password")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("movies:index")