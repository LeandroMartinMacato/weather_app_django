from django.shortcuts import render , redirect

from core.api_location import coordinatesAPI 
from core.api_weather import WeatherAPI
from .models import Location

from django.core.paginator import Paginator


# Create your views here.

def home(request):
    coordAPI = coordinatesAPI()
    weatherAPI = WeatherAPI()
    locations = Location.objects.values()
    # print(locations)

    locations_data = []
    for location in locations:
        # print(location)
        geoInfo = coordAPI.getCoords(location["name"])
        weatherInfo =  weatherAPI.getWeather(geoInfo["lat"] , geoInfo["long"])

        locations_data.append({
            "id" : location["id"],
            "name" : location["name"],
            "address": geoInfo["address"],
            "lat": geoInfo["lat"],
            "long": geoInfo["long"],
            "info": {
                "weather": weatherInfo["weather"],
                "description": weatherInfo["description"],
                "temperature": weatherInfo["temperature"],
                "min_temp": weatherInfo["low_temp"],
                "max_temp": weatherInfo["max_temp"],
            }
        })
        

    p = Paginator(locations_data , 3)
    page = request.GET.get('page')
    paged_data = p.get_page(page)


    # print(locations_data)
    context = {'paged_data': paged_data}
    return render(request , 'core/home.html' , context)

def location(request):

    context = {}
    return render(request , 'core/location.html' , context)