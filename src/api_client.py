import requests
import json
from datetime import datetime, timezone
import logging
import time

# Logging configuration 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# Load BASE_URL from config.json
with open ("config.json","r") as f:
    BASE_URL = json.load(f).get('BASE_URL')

def fetch_weather( city , api_key, retries = 3, backoff = 2, BASE_URL=BASE_URL ) :
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    for attempt in range (1, retries+1) :
        try:
            response  =  requests.get(BASE_URL,params = params , timeout=10)
            if(response.status_code == 200):
                data = response.json()
                data = parse_data(data,city)
                return data 
            else:
                logging.warning(f"Non 200 Status {response.status_code } : {response.text}")
        except Exception as e :
            logging.warning(f"Request Failed (attempt : {attempt}) : {e}")
        time.sleep(backoff * attempt)
    raise RuntimeError("Failed to fetch weather after retries")
    
def parse_data ( data,city ):
    weather_entry = {
            "timestamp" : datetime.now(timezone.utc).isoformat(),
            "city" : data.get('name',city),
            "temp" : data.get("main",{}).get('temp'),
            "humidity" : data.get("main",{}).get('humidity'),
            "description" : data.get('weather',[{}])[0].get('description')
        }
    return weather_entry 
        

