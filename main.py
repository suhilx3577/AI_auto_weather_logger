import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import csv

# Load Variable from .env
load_dotenv()
# Load API_KEY using getenv
API_KEY = os.getenv("API_KEY")


# Load BASE_URL from config.json
with open("config.json","r") as f:
    data = json.load(f)
    BASE_URL = data.get("BASE_URL")


city = input("Enter name of the City : ")

params = {
    "q" : city,
    "appid" : API_KEY,
    "units" : "metric"
}

response =  requests.get(BASE_URL,params=params)
data = response.json()
weather_entry = {
    "timestamp" : datetime.now().isoformat(),
    "city" : data.get('name'),
    "temp" : data.get("main",{}).get('temp'),
    "humidity" : data.get("main",{}).get('humidity'),
    "description" : data.get('weather',[{}])[0].get('description')
}


# Log the weather details into json file
def save_weather_json ( entry , filename):
    try: 
        with open (filename,"r+") as f :
            logs = json.load(f)

            logs.append(entry)
            f.seek(0)
            json.dump(logs,f,indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        with open (filename,"w") as f:
            json.dump([entry],f,indent=2)


# Log the Weather details into csv file
def save_weather_csv (entry,filename):
    try:
        with open ( filename,"a",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=entry.keys())
            writer.writerow(entry)
    except FileNotFoundError :
        with open(filename,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=entry.keys())
            writer.writeheader()
            writer.writerow(entry)

save_weather_csv(weather_entry,"weather_log.csv")
save_weather_json(weather_entry,"weather_log.json")
