from contactbook.contact_manager import (
    add_contact, update_contact, delete_contact, 
    search_contact, list_contacts, load_contacts, 
    save_contacts, CATEGORIES
)
from contactbook.validator import validate_email, validate_phone

FILENAME = "contacts.json"

def main():
    contacts = load_contacts(FILENAME)

    while True:
        print("\n📒 Personal Contact Book")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter 10-digit phone: ").strip()
            email = input("Enter email: ").strip()
            tags = set(input("Enter tags (comma-separated): ").strip().split(","))
            print(f"Available Categories: {', '.join(CATEGORIES)}")
            category = input("Enter category: ").strip().capitalize()

            if not validate_phone(phone):
                print("Invalid phone number.")
                continue
            if not validate_email(email):
                print("Invalid email.")
                continue
            if category not in CATEGORIES:
                print("Invalid category.")
                continue

            add_contact(contacts, name, phone, email, tags, category)

        elif choice == "2":
            name = input("Enter name to update: ").strip()
            phone = input("New phone (leave blank to skip): ").strip()
            email = input("New email (leave blank to skip): ").strip()
            update_contact(contacts, name, phone or None, email or None)

        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            delete_contact(contacts, name)

        elif choice == "4":
            name = input("Search name: ").strip()
            search_contact(contacts, name)

        elif choice == "5":
            list_contacts(contacts)

        elif choice == "6":
            save_contacts(FILENAME, contacts)
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
