from django.shortcuts import render, redirect
import requests
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from . import *
from django.http import HttpResponse


# Create your views here.

def index(request):
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=886705b4c1182eb1c69f28eb8c520e20'
    city = 'Canada'

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities :

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city ,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' :  r['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    # print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather_page.html',context)



def RegisterPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name='weather/register.html', context={"register_form": form})


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect('/weather_page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="weather/login.html", context={"login_form": form})