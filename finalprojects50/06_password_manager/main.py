# main.py

import getpass
from passwordmanager.manager import PasswordManager
from passwordmanager.security import generate_strong_password

def main():
    print("🔐 Welcome to Password Manager")

    key_input = getpass.getpass("Enter 16/24/32-byte encryption key (for AES): ")
    key = key_input.encode()
    pm = PasswordManager(key)
    pm.login()

    while True:
        print("\nMenu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Generate Strong Password")
        print("5. Show Weak Passwords")
        print("6. Save & Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password (leave blank to generate): ")
            if not password:
                password = generate_strong_password()
                print(f"Generated Password: {password}")
            pm.add_password(website, username, password)

        elif choice == "2":
            website = input("Website to retrieve: ")
            pm.retrieve_password(website)

        elif choice == "3":
            website = input("Website to delete: ")
            pm.delete_password(website)

        elif choice == "4":
            length = input("Password length (default 16): ").strip()
            try:
                length = int(length)
            except:
                length = 16
            print("Generated Strong Password:", generate_strong_password(length))

        elif choice == "5":
            print("Weak Passwords:")
            found = False
            for entry in pm.weak_passwords_generator():
                print(f"Website: {entry.website}, Password: {entry.password}")
                found = True
            if not found:
                print("No weak passwords found.")

        elif choice == "6":
            pm.save_passwords()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
