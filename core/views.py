from django.shortcuts import render , redirect

from core.api_location import coordinatesAPI 
from core.api_weather import WeatherAPI


# Create your views here.

def home(request):
    # coordAPI = coordinatesAPI()
    # print(coordAPI.getCoords("manila"))


    context = {}
    return render(request , 'core/home.html' , context)

def location(request):

    context = {}
    return render(request , 'core/location.html' , context)