import requests
import json

class WeatherAPI():
    def __init__(self):
        self.lat = None
        self.lon = None
        self.key = "72fbb4697eb1d570262776e341a53711"

    def setCoords(self , lat , lon):
        self.lat = lat
        self.lon = lon

    def getWeather(self):
        r = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=72fbb4697eb1d570262776e341a53711'
        ).json()
        
        weather = {
            "weather" : r["weather"][0]["main"],
            "description" : r["weather"][0]["description"],
            "temperature" : r["main"]["temp"],
        }
        return weather

if __name__ == "__main__":
    weatherAPI = WeatherAPI()
    print(weatherAPI.getWeather())
    