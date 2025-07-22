import csv
import os

CSV_FILE = "attendance_log.csv"

def generate_report(employee_name):
    if not os.path.exists(CSV_FILE):
        print("❌ Attendance file not found.")
        return

    print(f"\n📄 Attendance Report for: {employee_name}")
    print("-" * 40)
    found = False

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == employee_name.lower():
                print(f"📌 {row['Date']} at {row['Time']}")
                found = True

    if not found:
        print("No records found.")
