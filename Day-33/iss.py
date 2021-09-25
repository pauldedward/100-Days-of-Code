import requests
import datetime as dt
import smtplib

MY_LAT = '10.961695'
MY_LONG = '79.388115'
myPos = [float(MY_LAT), float(MY_LONG)]

def isIssCloser(myPos):
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()['iss_position']
    iss_longitude = float(data['longitude'])
    iss_latitude = float(data['latitude'])
    issPos = [iss_longitude, iss_latitude]
    
    if abs(issPos[0] - myPos[0]) <= 5.0 and abs(issPos[1] - myPos[1]) <= 5.0:
        return True
    
    return False

def isNight():
    parameters = {
        'lat': MY_LAT, 
        'lng': MY_LONG,
        'formatted': 0,
    }

    response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data['results']['sunrise']
    sunrise_hour = (int(sunrise.split('T')[1].split(':')[0]) + 5) % 24
    sunset = data['results']['sunset']
    sunset_hour = (int(sunset.split('T')[1].split(':')[0]) + 5) % 24
    time_now = dt.datetime.now()
    time_now_hour = int(time_now.hour)
    
    if time_now_hour <= sunrise_hour and time_now_hour >= sunset_hour:
        return True
    return False

while True:
    if isNight() and isIssCloser(myPos):
        print("It's night and ISS is close to you!")
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(user='myemail@gmail.com', password='password')
            smtp.sendmail(from_addr='myemail@gmail.com', to_addrs='otheremail@gmail.com', msg='It\'s night and ISS is close to you!')