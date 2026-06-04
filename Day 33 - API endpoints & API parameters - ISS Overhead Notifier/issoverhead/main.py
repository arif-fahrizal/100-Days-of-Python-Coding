import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -7.3558733, # Your latitude
MY_LONG = 109.6600728 # Your longitude

sender = "donquixotee7@gmail.com"
password = "bswgnxjgujhytgrm"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5

def is_nigh():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise
while True:
    time.sleep(60)
    if is_iss_overhead() and is_nigh():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            message = f"Subject:Look Up👆\n\nThe ISS is above you in the sky."
            connection.starttls()
            connection.login(sender, password)
            connection.sendmail(from_addr=sender, to_addrs=sender, msg=message)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



