import time

import requests
from datetime import datetime
import smtplib

MY_LAT = "YOUR LATITUDE"     # you can find yours here: https://www.latlong.net/
MY_LONG = "YOUR LONGITUDE"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
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

time_now = datetime.now()

print(sunrise, sunset)
print(iss_longitude, iss_latitude)

#If the ISS is close to my current position
while True:
    if iss_longitude + 5 == MY_LONG or iss_longitude - 5 == MY_LONG and iss_latitude + 5 == MY_LAT or iss_latitude - 5 == MY_LAT:
        if sunrise > time_now.hour > sunset:
            password = "YOURPASS"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="YOUR SEDNING ADDRESS", password=password)
                connection.sendmail(
                    from_addr="YOUR SENDING ADDRESS",
                    to_addrs="RECEIVER'S ADDRESS",
                    msg="Subject:ISS notification \n\n Hey! If the sky is clear you should be able to see ISS, it is just on top of your location now! \n Best Regards"
                )
#    print("Does timer wwork?")
    time.sleep(60)



