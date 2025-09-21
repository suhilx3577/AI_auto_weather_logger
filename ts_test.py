import os, sys
from datetime import datetime

print(">>> Python is running")
print("Working dir:", os.getcwd())
print("Python exe:", sys.executable)

with open(r"D:\AI Automation\Automation Projects\weather_logger\ts_output.txt", "a") as f:
    f.write(f"\n--- Task Scheduler Run ---\n")
    f.write(f"Time: {datetime.now()}\n")
    f.write(f"Working dir: {os.getcwd()}\n")
    f.write(f"Python exe: {sys.executable}\n")
