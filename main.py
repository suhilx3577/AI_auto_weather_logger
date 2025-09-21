from dotenv import load_dotenv
import os
from datetime import datetime
from src.api_client import fetch_weather
from src.utils import save_weather_csv, save_weather_json
import logging

import time

import os, logging

import os, sys

# Force working directory to project root
BASE_DIR = r"D:\AI Automation\Automation Projects\weather_logger"
os.chdir(BASE_DIR)
sys.path.insert(0, BASE_DIR)  # ensure imports work



# Debugging to check if task scheduler triggered the task or not.
logging.basicConfig(
    filename='weather_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Task Scheduler triggered script")
logging.info(f"Working directory: {os.getcwd()}")
logging.info(f"Python executable: {os.sys.executable}")



# Ensure logs folder exists
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

json_path = os.path.join(LOG_DIR, "weather_log.json")
csv_path = os.path.join(LOG_DIR, "weather_log.csv")


INTERVAL = 3

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
        save_weather_json(data,json_path=json_path)
        save_weather_csv(data,csv_path=csv_path)

    except Exception as e :
        logging.error("Weather Fetch Failed : %s", e)
        print("failed ",e)


# No Automation Code 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error : ",e)



# Python Side Automation
#1.  Use of Infinite Loop + time.sleep()
    # The simplest method.
    # Script stays alive, sleeps, wakes up, runs again.
# Code to run for Every INTERVAL Seconds

# if __name__ == "__main__":
#     try:
#         while True:
#             main()
#             logging.info(f" Sleeping for {INTERVAL} seconds")
#             time.sleep(INTERVAL)
#     except KeyboardInterrupt:
#         logging.info("Graceful Shutdown requested. Exiting.")


#2. Use of Schedule Library
# import time
# import schedule

# if __name__ == "__main__" :

#     # this says to run the function main for every INTERVAL seconds
#     schedule.every(INTERVAL).seconds.do(main)
#     try :
#         while True:
#             # this checks if is it time to run any job that is scheduled
#             schedule.run_pending()
#             # Pauses for a sec before running again. else runs 1000 time per second
#             time.sleep(1)
#             logging.info(f"Sleeping for {INTERVAL} seconds")
#     except KeyboardInterrupt :
#         logging.info("Graceful Shutdown requested. Exiting")