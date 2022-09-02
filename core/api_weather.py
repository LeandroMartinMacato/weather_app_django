import requests
import json

class WeatherAPI():
    def __init__(self):
        self.key = "72fbb4697eb1d570262776e341a53711"

    def getWeather(self , lat , long):
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={self.key}&units=metric'
        ).json()
        # print(r)
        
        weather = {
            "weather" : r["weather"][0]["main"],
            "description" : r["weather"][0]["description"],
            "temperature" : r["main"]["temp"],
            "low_temp" : r["main"]["temp_min"],
            "max_temp" : r["main"]["temp_max"]
        }
        return weather

if __name__ == "__main__":
    weatherAPI = WeatherAPI()
    print(weatherAPI.getWeather(14.5948914 , 120.9782618)) # Manila
    # print(weatherAPI.getWeather(40.7127281 , -74.0060152)) # New York
    
    