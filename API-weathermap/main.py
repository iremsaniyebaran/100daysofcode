import requests
from twilio.rest import Client

OWM_Endpoint = "https://sad4545gfg676"
api_key = "asdfghjklşi1234567890"
account_sid = "ASDFGHJKsadfg5467"
auth_token = "asdf456f55tt6t"

MAY_LAT = "51.90909"
MY_LON = "-09.7864"


weather_params = {
    "lat": MAY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = Client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_= "+9054632882",
        to= "+906888584",
    )
print(message.status)





































