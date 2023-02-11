from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", views.index),
    path("login/", views.loginPage,name="login"),
    path("register/", views.RegisterPage,name="register")
]