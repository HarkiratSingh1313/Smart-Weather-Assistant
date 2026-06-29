from Imports import *

def get_location():

    city = input("Enter city name: ")

    url = "http://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city,
        "limit": 5,
        "appid": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    if len(data) == 0:
        print("No matching city found.")
        return None

    print("\nPossible Locations:\n")

    for i, place in enumerate(data):

        state = place.get("state", "N/A")
        country = place.get("country", "N/A")

        print(f"{i+1}. {place['name']}, {state}, {country}")

    choice = int(input("\nSelect location number: ")) - 1

    latitude = data[choice]["lat"]
    longitude = data[choice]["lon"]

    return latitude, longitude, data[choice]["name"]





def current_weather(lat, lon):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    return response.json()