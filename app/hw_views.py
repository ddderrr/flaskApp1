# Rattananarin Yodruan (Fiw)
# 670510676
# sec001


import json
from urllib.request import urlopen
from flask import jsonify
from app import app

@app.route("/weather")
def hw01_localweather():
    return app.send_static_file("hw01_localweather.html")


def read_web_page(url):
    assert url.startswith("https://")
    with urlopen(url) as res:
        return res.read()




@app.route("/api/weather")
def api_weather():
    url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=18.8037949&longitude=98.9499454&hourly=pm10,pm2_5,us_aqi&current=us_aqi,pm10,pm2_5"   
    response = read_web_page(url)
    
    data = json.loads(response)
 
    current_time = data["current"]["time"]
    hourly = data["hourly"]
    times = hourly["time"]
    
    idx = times.index(current_time)
    
    current = {
        "AQI_US" : hourly["us_aqi"][idx],
        "PM10" : hourly["pm10"][idx],
        "PM2.5" : hourly["pm2_5"][idx], 
        "Time" : times[idx],
    }
    next_hr = {
        "AQI_US" : hourly["us_aqi"][idx+1], 
        "PM10" : hourly["pm10"][idx+1],
        "PM2.5" : hourly["pm2_5"][idx+1],
        "Time" : times[idx+1],
    }
    return json.dumps({"current": current, "next_hr": next_hr})



