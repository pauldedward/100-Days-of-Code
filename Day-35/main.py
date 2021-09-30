import os
import requests
from dotenv import load_dotenv
load_dotenv()

endpoint = 'https://api.openweathermap.org/data/2.5/onecall' 
api_key=os.getenv('API_KEY')
lat = 10.968223 
long = 79.275114
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

response = requests.get(endpoint, params={'lat': lat, 'lon': long, 'exclude': 'current,minutely,daily', 'appid': api_key})
response.raise_for_status()

data = response.json()
hour_data = data['hourly']

for hour in range(14):
    hour_weather = hour_data[hour]['weather'][0]
    if hour_weather['id'] < 600:
        print(f'{hour}: {hour_weather["description"]}')
