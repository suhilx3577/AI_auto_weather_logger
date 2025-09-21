import json 
import csv
import os

 # Log the weather details into json file
def save_weather_json ( entry , json_path):
    try: 
        with open (json_path,"r+") as f :
            logs = json.load(f)

            logs.append(entry)
            f.seek(0)
            json.dump(logs,f,indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        with open (json_path,"w") as f:
            json.dump([entry],f,indent=2)



# Log the Weather details into csv file
def save_weather_csv (entry,csv_path):
    try:
        with open ( csv_path,"a",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=entry.keys())
            writer.writerow(entry)
    except FileNotFoundError :
        with open(csv_path,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=entry.keys())
            writer.writeheader()
            writer.writerow(entry)
