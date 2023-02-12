from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", views.loginPage,name="login"),
    path("weather_page/", views.index),
    path("register/", views.RegisterPage,name="register")
]