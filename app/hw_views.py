# Rattananarin Yodruan (Fiw)
# 670510676
# sec001


import json
from urllib.request import urlopen
from flask import jsonify
from app import app
from flask import render_template
def read_web_page(url):
    assert url.startswith("https://")
    with urlopen(url) as res:
        return res.read()
import time



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

@app.route("/hw03/prcp/")
def hw03_prcp():
    # construct API URL with lat/lon and date range
    # fetch data using urlopen
    # process daily precipitation data
    # compute day of week for each date
    # generate trend arrows
    # assign weekend class
    # organize by month (columns)

    url3 = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=7.0084&longitude=100.4767&start_date=2025-11-01&end_date=2025-12-07&daily=precipitation_sum&hourly=temperature_2m&timezone=Asia%2FBangkok"
    
    response = read_web_page(url3)
    data = json.loads(response)
    la = data["latitude"]
    # assert url3.startswith("https://")
    # with urlopen(url3) as res:
    #     return res.read()   
    return render_template('lab03/hw03_prcp.html', data = ...)
