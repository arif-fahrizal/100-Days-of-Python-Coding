import requests

LAT = -7.4508189
LONG = 109.5246085
API_KEY = "PUT_YOUR_API_KEY_HERE"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

OWM_Parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=OWM_Parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]['id']

    if condition_code < 700:
        will_rain =  True

if will_rain:
    print("Bring Umbrella")