import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY")

weather_params = {
    "lat": 42.697708,  #your lat 
    "lon": 23.321867,	#your lon 
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

id = weather_data["hourly"][0]["weather"][0]["id"]

twelve_hours_list = weather_data["hourly"][0:11]

will_rain = False
id_s = []
for hour in twelve_hours_list:
    id = hour["weather"][0]["id"]
    if int(id) < 8000:
        will_rain = True
    id_s.append(id)

if will_rain:
    message = client.messages \
        .create(
        body="Will rain today! Take care! 💖",
        from_='+1phone number',
        to='+yourphonehumber'
    )
#    print(message.status)
#    print(message.sid)
