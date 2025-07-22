import json
import os
from datetime import datetime

VAULT_FILE = "snippets.json"
TAG_DIR = "tags"

def load_snippets():
    if not os.path.exists(VAULT_FILE) or os.path.getsize(VAULT_FILE) == 0:
        return []
    with open(VAULT_FILE, "r") as file:
        return json.load(file)


def save_snippets(snippets):
    with open(VAULT_FILE, "w") as file:
        json.dump(snippets, file, indent=4)

def add_snippet():
    title = input("Title: ")
    description = input("Description: ")
    code = input("Code Snippet:\n")
    tags = input("Tags (comma-separated): ").split(",")

    snippet = {
        "title": title,
        "description": description,
        "code": code,
        "tags": [tag.strip() for tag in tags],
        "added_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    snippets = load_snippets()
    snippets.append(snippet)
    save_snippets(snippets)
    print("✅ Snippet added successfully.")

    # Advanced: Store each snippet in tag folders as .txt
    os.makedirs(TAG_DIR, exist_ok=True)
    for tag in snippet['tags']:
        tag_folder = os.path.join(TAG_DIR, tag)
        os.makedirs(tag_folder, exist_ok=True)
        file_path = os.path.join(tag_folder, f"{title.replace(' ', '_')}.txt")
        with open(file_path, "w") as f:
            f.write(f"Title: {title}\nDescription: {description}\nCode:\n{code}")
        print(f"🗂️  Saved under tag folder: {tag}/")

def search_snippets_by_title():
    keyword = input("Enter title keyword: ").lower()
    snippets = load_snippets()
    found = False
    for s in snippets:
        if keyword in s["title"].lower():
            print_snippet(s)
            found = True
    if not found:
        print("No matching snippets found.")

def search_snippets_by_tag():
    keyword = input("Enter tag: ").strip().lower()
    snippets = load_snippets()
    found = False
    for s in snippets:
        if keyword in [t.lower() for t in s["tags"]]:
            print_snippet(s)
            found = True
    if not found:
        print("No matching tag found.")

def print_snippet(s):
    print("\n📌 Title:", s['title'])
    print("📝 Description:", s['description'])
    print("🏷️ Tags:", ', '.join(s['tags']))
    print("📅 Added On:", s['added_on'])
    print("💻 Code:\n", s['code'])
