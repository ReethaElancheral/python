# journal/exporter.py

import os
import json
from datetime import datetime

def export_entries():
    entries = []
    for filename in os.listdir("journal/data"):
        if filename.endswith(".txt"):
            with open(os.path.join("journal/data", filename), "r") as file:
                content = file.read()
                entries.append({"date": filename[:-4], "content": content})
    with open("journal_entries.json", "w") as json_file:
        json.dump(entries, json_file, indent=4)
    print("Entries exported to journal_entries.json")
