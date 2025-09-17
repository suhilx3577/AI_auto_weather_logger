import json 
import csv
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
