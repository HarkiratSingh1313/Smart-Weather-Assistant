from Current_Weather import *
from Forecast import *
from Display import *

location = get_location()

if location:

    lat, lon, city = location

    print(f"\nSelected City: {city}")

    weather = current_weather(lat, lon)

    forecast = forecast_weather(lat, lon)

    show_current_weather(weather)

    show_forecast(forecast)