import json
import csv
import os

DATA_FILE = "contacts.json"
CSV_FILE = "contacts_export.csv"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def export_to_csv(contacts):
    if not contacts:
        print("No contacts to export.")
        return

    with open(CSV_FILE, "w", newline='') as csvfile:
        fieldnames = ["name", "phone", "email", "category"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
    print(f"Contacts exported successfully to {CSV_FILE}")
