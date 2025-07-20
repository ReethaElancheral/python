import json
import os

CATEGORIES = ("Family", "Friends", "Work", "Other")

def load_contacts(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

def save_contacts(filename, contacts):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts, name, phone, email, tags, category):
    if name in contacts:
        print("Contact already exists.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": list(tags),
        "category": category
    }
    print(f"Contact '{name}' added.")

def update_contact(contacts, name, phone=None, email=None):
    if name not in contacts:
        print("Contact not found.")
        return

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print(f"Contact '{name}' updated.")

def delete_contact(contacts, name):
    if contacts.pop(name, None):
        print(f"Deleted '{name}'")
    else:
        print("Contact not found.")

def search_contact(contacts, name):
    if name in contacts:
        c = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"Tags: {', '.join(c['tags'])}")
        print(f"Category: {c['category']}")
    else:
        print("Contact not found.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- All Contacts ---")
    for name in sorted(contacts.keys()):
        c = contacts[name]
        print(f"{name} - {c['phone']} ({c['category']})")
