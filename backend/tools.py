import os
import requests

def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    res = requests.get(url, params=params)
    data = res.json()

    if res.status_code != 200:
        return f"Weather error: {data.get('message')}"

    return (
        f"Weather in {city.title()}: "
        f"{data['weather'][0]['description']}, "
        f"{data['main']['temp']}°C"
    )
