import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 169
AGE = 19

APP_ID = os.environ["c97155c0"]
API_KEY = os.environ["f6c86cdec21e2bf972febc299582bce9"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint =os.environ["https://api.sheety.co/bdef0505ad84b457aaa0c1c37c86ab98/myWorkoutsDosyasınınKopyası/workouts"]

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['aXJlbTphYmMxMjM=']}"
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

print(sheet_response.text)











