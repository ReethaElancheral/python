import json
import os

FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_contacts(contacts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

def create_contact():
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()

    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact already exists.")
            return
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added.")

def read_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

def update_contact():
    name = input("Enter the name of contact to update: ").strip()
    contacts = load_contacts()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name.lower():
            new_phone = input(f"New phone (current: {c['phone']}): ").strip()
            new_email = input(f"New email (current: {c['email']}): ").strip()
            if new_phone:
                contacts[i]['phone'] = new_phone
            if new_email:
                contacts[i]['email'] = new_email
            save_contacts(contacts)
            print("✅ Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of contact to delete: ").strip()
    contacts = load_contacts()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name.lower():
            contacts.pop(i)
            save_contacts(contacts)
            print("✅ Contact deleted.")
            return
    print("Contact not found.")
