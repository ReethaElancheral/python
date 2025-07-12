# 2. User Registration & Login System

# Concepts: strings, lists, functions, while.
# Register users with username + password (string handling).
# Store users in a list of dicts or nested list.
# Login using a while loop (limit attempts).
# Functions for login, register, show users.

users = []  


def register():
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    for user in users:
        if user["username"] == username:
            print("Username already taken. Try a different one.")
            return

    users.append({"username": username, "password": password})
    print(f"User '{username}' registered successfully.")


def login():
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

     
        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Login successful. Welcome, {username}!")
                return

        attempts -= 1
        print(f"Incorrect credentials. Attempts remaining: {attempts}")

    print("Login failed. Too many incorrect attempts.")


def show_users():
    if not users:
        print("No users registered.")
    else:
        print("\nRegistered Users:")
        for user in users:
            print(f"Username: {user['username']}")


while True:
    print("\n=== User System Menu ===")
    print("1. Register")
    print("2. Login")
    print("3. Show Users")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        show_users()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 4.")
