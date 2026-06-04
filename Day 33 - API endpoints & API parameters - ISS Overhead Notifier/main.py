import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

parameters = {
    "lat": -7.3558733,
    "lng": 109.6600728,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

data = response.json()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
