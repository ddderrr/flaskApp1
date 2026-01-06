# Rattananarin Yodruan (Fiw)
# 670510676
# sec001


import json
from urllib.request import urlopen
from flask import jsonify, redirect, url_for
from app import app
from flask import render_template
from datetime import datetime
from flask import send_from_directory

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


@app.route("/hw03/prcp/")
def hw03_prcp():
    url3 = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=7.0084&longitude=100.4767&start_date=2025-11-01&end_date=2025-12-15&daily=precipitation_sum&hourly=temperature_2m&timezone=Asia%2FBangkok"
    response = read_web_page(url3)
    data = json.loads(response)

    dates = data["daily"]["time"]
    prcp  = data["daily"]["precipitation_sum"]

    forecast = [] 

    for i, date_str in enumerate(dates):
        rain = prcp[i]

        forecast.append({
            "date": date_str,
            "prcp": rain
        })

    months = {}

    for i, date_str in enumerate(dates):
        date_object = datetime.strptime(date_str, "%Y-%m-%d")
        date_of_week = date_object.strftime('%a')[:2]
        month_key = date_object.strftime("%b %Y")


        trend = ""
        if i == 0:
            trend = ""
        if i > 0:
            curr_prcp = prcp[i]
            prev_prcp = prcp[i-1]
            if curr_prcp > prev_prcp:
                trend = "↑"
            elif curr_prcp < prev_prcp:
                trend = "↓"
            elif curr_prcp == prev_prcp:
                trend = "↔"

        if month_key not in months:
            months[month_key] = []

        months[month_key].append({
            "day": f"{date_object.day:02d}",
            "days": date_of_week,
            "prcp": prcp[i],
            "trend": trend
        })
        trend_perday = max(len(day) for day in months.values()) if months else 0
    return render_template('lab03/hw03_prcp.html',months=months, trend_perday=trend_perday, date_of_week = date_of_week)

@app.route("/hw04")
def hw04_rwd():
    return send_from_directory('static','hw04_rwd.html')


@app.route("/hw05/aqicard")
def hw05_aqicard():
    token = "dee5632cb96ad0c87e18dee90294c6229ba77ecf"
    
    cities_config = [
        {"url": "chiang-mai", "display_name": "Chiang Mai"},
        {"url": "ubon-ratchathani", "display_name": "Ubon Ratchathani"},
        {"url": "phuket", "display_name": "Phuket"},
        {"url": "bangkok", "display_name": "Bangkok"}
    ]
    
    city_data = []
    
    for city_config in cities_config:
        url = f"https://api.waqi.info/feed/{city_config['url']}/?token={token}"
        response = read_web_page(url)
        data = json.loads(response)
        
        aqi = data["data"]["aqi"]
        time = data["data"]["time"]["s"]
        
        date_part = time.split()[0]
        date_obj = datetime.strptime(date_part, "%Y-%m-%d")
        day = date_obj.strftime("%d %B")
        year = date_obj.strftime("%Y")
        
        if aqi <= 50:
            status = "Good"
            bg_class = "bg-green"
            icon = "good.png"
            img_class = "img-good"
        elif aqi <= 100:
            status = "Moderate"
            bg_class = "bg-yellow"
            icon = "moderate.png"
            img_class = "img-moderate"
        elif aqi <= 150:
            status = "Unhealthy for sensitive group"
            bg_class = "bg-orange"
            icon = "unhealthy-sensitive.png"
            img_class = "img-unhealthy"
        else:
            status = "Unhealthy"
            bg_class = "bg-red"
            icon = "unhealthy.png"
            img_class = "img-unhealthy2"
        
        city_data.append({
            'name': city_config['display_name'],
            'aqi': aqi,
            'date': day,
            'year': year,
            'status': status,
            'bg_class': bg_class,
            'icon': icon,
            'img_class': img_class
        })
        
    timestamp = int(datetime.now().timestamp())
    
    return render_template('hw05_aqicard.html', cities=city_data, timestamp=timestamp)

@app.route("/hw06/register/", methods=["GET", "POST"])
def hw06_register():
    form = form.courseForm()    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data      
        confirm_password = form.confirm_password.data   
        return redirect(url_for('hw06_users'))
    return render_template('/hw06_register.html', form=form)
        