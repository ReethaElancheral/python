import json
import os

FILENAME = "diary_entries.json"

def load_entries():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        data = json.load(f)
        for entry in data:
            entry["tags"] = set(entry["tags"])
        return data

def save_entries(entries):
    data = [{"date": e["date"], "text": e["text"], "tags": list(e["tags"])} for e in entries]
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)

def add_entry(entries, date, text, tags):
    entries.append({"date": date, "text": text, "tags": tags})
    print("Entry added.")

def edit_entry(entries, date):
    for entry in entries:
        if entry["date"] == date:
            print(f"Old text: {entry['text']}")
            entry["text"] = input("New text: ").strip()
            new_tags = input("New tags (comma-separated): ").strip()
            entry["tags"] = set(new_tags.split(","))
            print("Entry updated.")
            return
    print("Entry not found.")

def delete_entry(entries, date):
    original_len = len(entries)
    entries[:] = [e for e in entries if e["date"] != date]
    if len(entries) < original_len:
        print("Entry deleted.")
    else:
        print("Entry not found.")
