import geocoder  # pip install geocoder
from geopy.geocoders import Nominatim  # pip install geopy
import pyowm  # pip install pyowm
from pyowm import OWM
import os
from dotenv import load_dotenv

load_dotenv()

# Function for weather

def getCorrdinates():
    g = geocoder.ip('me')
    return g.lat, g.lng


def getPlace():
    cord = getCorrdinates()
    lat = cord[0]
    lon = cord[1]
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.reverse(cord)
    address = location.raw['address'] 
    city = address.get('city', '')
    country = address.get('country','')
    return city,country


def getWeather():
    location = getPlace()
    city = location[0]
    country = location[1]
    api =  os.getenv("OWM_API_KEY")
    owm = OWM(api)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city+","+country)
    w = observation.weather
    current_temp = str(w.temperature('celsius').get('temp'))
    current_status = w.detailed_status
    return "Temperature is "+current_temp+"celsius and the sky is "+current_status


