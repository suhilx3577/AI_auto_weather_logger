from dotenv import load_dotenv
import os
from datetime import datetime
from src.api_client import fetch_weather
from src.utils import save_weather_csv, save_weather_json
import logging

import time

INTERVAL = 2

# Load Variable from .env
load_dotenv()
# Load API_KEY using getenv
API_KEY = os.getenv("API_KEY")
city = os.getenv('city')
def main() :
    if not API_KEY:
        print("ERROR: OPENWEATHER_API_KEY missing. Put it in .env file.")
        return
    try :
        # Fetch weather function call
        data = fetch_weather(city,API_KEY)
        save_weather_json(data,"logs/weather_log.json")
        save_weather_csv(data,"logs/weather_log.csv")

    except Exception as e :
        logging.error("Weather Fetch Failed : %s", e)
        print("failed ",e)


# Python Side Automation
#1.  Use of Infinite Loop + time.sleep()
    # The simplest method.
    # Script stays alive, sleeps, wakes up, runs again.
# Code to run for Every INTERVAL Seconds
if __name__ == "__main__":
    try:
        while True:
            main()
            logging.info(f" Sleeping for {INTERVAL} seconds")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        logging.info("Graceful Shutdown requested. Exiting.")


#2. Use of Schedule Library
import time
import schedule

if __name__ == "__main__" :

    # this says to run the function main for every INTERVAL seconds
    schedule.every(INTERVAL).seconds.do(main)
    try :
        while True:
            # this checks if is it time to run any job that is scheduled
            schedule.run_pending()
            # Pauses for a sec before running again. else runs 1000 time per second
            time.sleep(1)
            logging.info(f"Sleeping for {INTERVAL} seconds")
    except KeyboardInterrupt :
        logging.info("Graceful Shutdown requested. Exiting")