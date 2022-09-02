from geopy.geocoders import Nominatim

class coordinatesAPI():
    def __init__(self):
        self.loc = Nominatim(user_agent="GetLoc")
        self.getLoc = None

    def getCoords(self , location):
        self.getLoc = self.loc.geocode(location)
        name = self.getLoc.address
        lat = self.getLoc.latitude
        long = self.getLoc.longitude

        return {
            "name" : name,
            "lat" : lat,
            "long" : long
        }

if __name__ == "__main__":
    coordAPI = coordinatesAPI()
    print(coordAPI.getCoords("manila"))
