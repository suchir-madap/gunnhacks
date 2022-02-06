


import requests

def check_conditions(zipcode):

    if type(zipcode) != int:
        raise Exception

    weather_call = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=bd85bd1838a37384556ace68c693d987")

    temp = weather_call.json()["main"]["temp"]
    conditions = weather_call.json()["weather"]["id"]

    return [temp, conditions]

print(check_conditions(27519))
    
