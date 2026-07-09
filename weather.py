# weather.py
# This file handles ONLY the "talking to the internet" part.
# It does not deal with any GUI/screen stuff — that's main.py's job.

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local testing)
load_dotenv()

# Get API key from environment variable (secure for cloud deployment)
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# Fallback API key if environment variable is not set
if not API_KEY:
    API_KEY = "9aac7ae37f68e3d23dbfcc5f0fa4a1ff"

# Base URL for OpenWeatherMap's "current weather" endpoint.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Takes a city name (text) as input.
    Returns a dictionary with weather info if successful,
    or a dictionary with an 'error' key if something went wrong.
    """

    # These are the parameters we send along with our request.
    # 'q' = city name, 'appid' = our API key, 'units' = metric (Celsius, not Kelvin)
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send a GET request to the OpenWeatherMap server with our parameters.
        response = requests.get(BASE_URL, params=params)

        # response.status_code tells us if the request succeeded (200 = OK).
        # If the city doesn't exist, OpenWeatherMap returns 404.
        if response.status_code == 404:
            return {"error": "City not found. Please check the spelling and try again."}

        # If it's any other kind of failure (500, 401 invalid key, etc.)
        if response.status_code != 200:
            return {"error": f"Something went wrong (Error code: {response.status_code})."}

        # If we reach here, the request was successful.
        # response.json() converts the server's reply (JSON text) into a Python dictionary.
        data = response.json()

        # Now we pick out only the specific pieces of data we care about,
        # and organize them into a clean dictionary to send back to main.py.
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except requests.exceptions.ConnectionError:
        # This runs if there is no internet connection at all.
        return {"error": "No internet connection. Please check your network."}

    except Exception as e:
        # This is a catch-all for any other unexpected error.
        return {"error": f"An unexpected error occurred: {e}"}
