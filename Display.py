from Imports import *
from Recommendations import *

def show_current_weather(weather):

    print("\n==============================")
    print("CURRENT WEATHER")
    print("==============================")

    print("Temperature:",
          weather["main"]["temp"], "°C")

    print("Feels Like:",
          weather["main"]["feels_like"], "°C")

    print("Humidity:",
          weather["main"]["humidity"], "%")

    print("Pressure:",
          weather["main"]["pressure"], "hPa")

    print("Wind Speed:",
          weather["wind"]["speed"], "m/s")

    print("Visibility:",
          weather["visibility"]/1000, "km")

    print("Condition:",
          weather["weather"][0]["description"])

    timezone_offset = weather["timezone"]

    city_timezone = timezone(timedelta(seconds=timezone_offset))

    sunrise = datetime.fromtimestamp(
        weather["sys"]["sunrise"],
        tz=timezone.utc
    ).astimezone(city_timezone)

    sunset = datetime.fromtimestamp(
        weather["sys"]["sunset"],
        tz=timezone.utc
    ).astimezone(city_timezone)

    print("Sunrise:",
          sunrise.strftime("%I:%M %p"))

    print("Sunset:",
          sunset.strftime("%I:%M %p"))

    print("\nRecommendation")

    print(clothing_advice(weather["main"]["temp"]))

    print(umbrella_advice(
        weather["weather"][0]["description"]
    ))




def show_forecast(forecast):

    print("\n==============================")
    print("5 DAY FORECAST")
    print("==============================")

    for item in forecast["list"]:

        time = item["dt_txt"].split()[1]

        if time == "12:00:00":

            date = datetime.strptime(
                item["dt_txt"],
                "%Y-%m-%d %H:%M:%S"
            )

            print("=" * 45)
            print(f"📅 Date        : {date.strftime('%d %b %Y')}")
            print(f"🕛 Time        : {date.strftime('%I:%M %p')}")
            print(f"🌡 Temperature : {item['main']['temp']} °C")
            print(f"🤗 Feels Like  : {item['main']['feels_like']} °C")
            print(f"💧 Humidity    : {item['main']['humidity']} %")
            print(f"🌬 Wind Speed  : {item['wind']['speed']} m/s")
            print(f"☁ Condition   : {item['weather'][0]['description']}")
            print("=" * 45)