import csv
from datetime import datetime
import os

CSV_FILE = "attendance_log.csv"

def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])
        writer.writerow([name, date_str, time_str])
    print(f"✅ Attendance marked for {name} at {time_str} on {date_str}")
