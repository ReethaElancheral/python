import json
import os

FILENAME = "profiles.json"

def load_profiles():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_profiles(profiles):
    with open(FILENAME, "w") as file:
        json.dump(profiles, file, indent=4)

def add_profile():
    name = input("Name: ")
    email = input("Email: ")
    age = input("Age: ")
    phone = input("Phone: ")
    profile = {
        "name": name,
        "email": email,
        "age": age,
        "phone": phone
    }
    profiles = load_profiles()
    profiles.append(profile)
    save_profiles(profiles)
    print("✅ Profile added.")

def view_profiles():
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
        return
    print("\n📋 All Profiles:")
    for idx, profile in enumerate(profiles, 1):
        print(f"{idx}. {profile['name']} | {profile['email']} | Age: {profile['age']} | Phone: {profile['phone']}")

def update_profile():
    profiles = load_profiles()
    if not profiles:
        print("No profiles to update.")
        return
    view_profiles()
    try:
        index = int(input("Enter profile number to update: ")) - 1
        if index < 0 or index >= len(profiles):
            raise IndexError
        print("Leave field blank to keep current value.")
        name = input(f"Name ({profiles[index]['name']}): ") or profiles[index]['name']
        email = input(f"Email ({profiles[index]['email']}): ") or profiles[index]['email']
        age = input(f"Age ({profiles[index]['age']}): ") or profiles[index]['age']
        phone = input(f"Phone ({profiles[index]['phone']}): ") or profiles[index]['phone']

        profiles[index].update({
            "name": name,
            "email": email,
            "age": age,
            "phone": phone
        })
        save_profiles(profiles)
        print("✅ Profile updated.")
    except (IndexError, KeyError, ValueError):
        print("❌ Invalid selection.")

def delete_profile():
    profiles = load_profiles()
    if not profiles:
        print("No profiles to delete.")
        return
    view_profiles()
    try:
        index = int(input("Enter profile number to delete: ")) - 1
        if index < 0 or index >= len(profiles):
            raise IndexError
        deleted = profiles.pop(index)
        save_profiles(profiles)
        print(f"✅ Profile '{deleted['name']}' deleted.")
    except (IndexError, KeyError, ValueError):
        print("❌ Invalid selection.")
