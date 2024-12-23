import requests
from datetime import datetime as dt

MY_LATITUDE = 51.507351
MY_LONGITUDE = -0.127758


def get_current_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return iss_longitude, iss_latitude


def is_iss_overhead():
    iss_latitude = iss_position[0]
    iss_longitude = iss_position[1]

    # check if ISS latitude & longitude are within 5 degrees of my latitude & longitude
    if (MY_LATITUDE - 5) <= iss_latitude <= (MY_LATITUDE + 5):
        if (MY_LONGITUDE - 5) <= iss_longitude <= (MY_LONGITUDE + 5):
            return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = dt.now().hour

    if current_hour <= sunrise_hour or current_hour >= sunset_hour:
        return True


iss_position = get_current_iss_position()
