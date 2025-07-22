import os
from datetime import datetime

DIARY_DIR = "diary_entries"

def get_filename(date=None):
    if not os.path.exists(DIARY_DIR):
        os.makedirs(DIARY_DIR)
    if date:
        return os.path.join(DIARY_DIR, f"{date}.txt")
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(DIARY_DIR, f"{today}.txt")

def write_entry():
    path = get_filename()
    try:
        with open(path, "a") as file:
            print("\n📝 Write your diary entry. Type 'END' to finish:")
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                file.write(line + "\n")
        print(f"✅ Entry saved to {path}")
    except Exception as e:
        print(f"❌ Error writing entry: {e}")

def read_entry():
    date = input("📅 Enter date to read (YYYY-MM-DD): ")
    path = get_filename(date)
    try:
        with open(path, "r") as file:
            print(f"\n📖 Diary entry for {date}:\n")
            print(file.read())
    except FileNotFoundError:
        print("❌ No entry found for that date.")
    except Exception as e:
        print(f"❌ Error reading entry: {e}")

def edit_entry():
    date = input("📅 Enter date to edit (YYYY-MM-DD): ")
    path = get_filename(date)
    try:
        with open(path, "r") as file:
            old_content = file.read()
        print(f"\n📃 Current entry:\n{old_content}")
        print("\n✏️ Enter new content. Type 'END' to save:")
        new_lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            new_lines.append(line)
        with open(path, "w") as file:
            file.write("\n".join(new_lines) + "\n")
        print(f"✅ Entry updated for {date}")
    except FileNotFoundError:
        print("❌ No entry found for that date.")
    except Exception as e:
        print(f"❌ Error editing entry: {e}")
