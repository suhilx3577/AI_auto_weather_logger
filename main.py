import requests
from dotenv import load_dotenv
import os
import json

# Load Variable from .env
load_dotenv()
# Load API_KEY using getenv
API_KEY = os.getenv("API_KEY")


# Load BASE_URL from config.json
with open("config.json","r") as f:
    data = json.load(f)
    BASE_URL = data.get("BASE_URL")
    print(BASE_URL)


city = input("Enter name of the City : ")

params = {
    "q" : city,
    "appid" : API_KEY,
    "units" : "metric"
}

response =  requests.get(BASE_URL,params=params)
data = response.json()
print(data.get("main"))

