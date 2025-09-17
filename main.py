import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import csv
from src.api_client import fetch_weather
from src.utils import save_weather_csv, save_weather_json
import logging

# Load Variable from .env
load_dotenv()
# Load API_KEY using getenv
API_KEY = os.getenv("API_KEY")

def main() :
    if not API_KEY:
        print("ERROR: OPENWEATHER_API_KEY missing. Put it in .env file.")
        return
    try :
        # Fetch weather function call
        city = input("Enter name of the City : ")
        data = fetch_weather(city,API_KEY)
        save_weather_json(data,"logs/weather_log.json")
        save_weather_csv(data,"logs/weather_log.csv")

    except Exception as e :
        logging.error("Weather Fetch Failed : %s", e)
        print("failed ",e)

if __name__ == "__main__":
    main()