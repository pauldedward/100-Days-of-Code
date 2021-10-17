from json import load
import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('APPID')
API_KEY = os.getenv('APIKEY')
BEARER = os.getenv('BEARER')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/9b7736d1b124bc3ab79a46fe4aff29ec/workoutTracking/workouts"

query = input("Enter the Exercises: ")

nutri_body = {
    "query": query,
    "gender": "male",
    "weight_kg": 75.5,
    "height_cm": 177,
    "age": 22,
}

res = requests.post(url=nutritionix_url, headers=headers, json=nutri_body)
exercise_data = res.json()["exercises"]

sheety_headers = {
    'Authorization': 'Bearer {}'.format(BEARER),
    "Content-Type": "application/json"
}

print(exercise_data)
for ex in exercise_data:
    workout_body = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": ex["name"].title(),
            "duration": float(ex["duration_min"]),
            "calories": float(ex["nf_calories"]),
        }
    }

    res = requests.post(url=sheety_url, json=workout_body, headers=sheety_headers)
    print(res.text)
