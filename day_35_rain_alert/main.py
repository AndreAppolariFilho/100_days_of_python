import requests
import datetime
api_key = "60fddc9ee760899bfdd35de48edae65f"

param = {
    "lat": -47.384740,
    "lon": -22.386440,
    "exclude":"current,daily,minutely",
    "appid": "60fddc9ee760899bfdd35de48edae65f"
}

url = "https://api.openweathermap.org/data/2.5/onecall"

req = requests.get(url, params=param)
req.raise_for_status()
weather_data = req.json()
rainy_hours = []
now = datetime.datetime.now()
for index, hour in enumerate(weather_data["hourly"][:12:]):
  if int(hour["weather"][0]["id"]) < 700:
    rainy_hours.append((now + datetime.timedelta(hours=index)).time())
