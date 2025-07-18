# journal/entry.py

import os
from datetime import datetime

def get_entry_filename():
    return datetime.now().strftime("%Y-%m-%d") + ".txt"

def log_entry(content):
    filename = get_entry_filename()
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a") as file:
        file.write(content + "\n")
    print(f"Entry logged in {filename}")
