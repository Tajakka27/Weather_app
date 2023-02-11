from django.shortcuts import render
import requests
from .models import *
from .forms import *
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

def loginPage(request):
    return render(request,'weather/login.html')

def RegisterPage(request):
    return render(request,'weather/register.html')