from django.shortcuts import render , redirect

from core.api_location import coordinatesAPI 
from core.api_weather import WeatherAPI
from .models import Location

from django.core.paginator import Paginator

import logging
import datetime

logger = logging.getLogger(__name__)


# Create your views here.

def home(request):
    coordAPI = coordinatesAPI()
    weatherAPI = WeatherAPI()
    locations = Location.objects.values()

    locations_data = []
    for location in locations:
        if location["address"] == None or location["address"] == "" :
            print(f"{location['name']} doesnt have coordinates")
            try:
                geoInfo = coordAPI.getCoords(location["name"])
            except Exception as e:
                print(e)
                logger.warning(f'Failed to get location coordinates data for "{location["name"]}" - {str(datetime.datetime.now())} ')
                continue
            location_db_data = Location.objects.get(id = location["id"])
            location_db_data.address = geoInfo["address"]
            location_db_data.lat = geoInfo["lat"]
            location_db_data.long = geoInfo["long"]
            location_db_data.save()
        else:
            geoInfo = {
                "address" : location["address"],
                "lat" : location["lat"],
                "long" : location["long"]
            }

        try:
            weatherInfo =  weatherAPI.getWeather(geoInfo["lat"] , geoInfo["long"])
        except Exception as e:
            print(e)
            logger.warning(f'Failed to get weather data for "{location["name"]}" - {str(datetime.datetime.now())} ')
            continue


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
                "min_temp": round(int(weatherInfo["low_temp"])),
                "max_temp": round(int(weatherInfo["max_temp"])),
            }
        })
        

    p = Paginator(locations_data , 5)
    page = request.GET.get('page')
    paged_data = p.get_page(page)

    context = {'paged_data': paged_data}
    return render(request , 'core/home.html' , context)