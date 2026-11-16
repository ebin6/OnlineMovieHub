from django.urls import path
from accounts import views

app_name="accounts"

urlpatterns=[
    path("register/",views.signUp,name="register"),
    path("login/",views.signIn,name="login"),
    path("logout/",views.logout,name="logout")
]