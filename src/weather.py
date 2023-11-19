import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_longitude(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        longitude = data['coord']['lon']
        return int(longitude)
    else:
        return None


def get_latitude(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = data['coord']['lat']
        return int(latitude)
    else:
        return None
