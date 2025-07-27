from contacts.contact_manager import (
    add_contact, delete_contact, edit_contact,
    search_contacts, group_contacts, view_contacts
)
from contacts.file_handler import load_contacts, save_contacts, export_to_csv

def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Export to CSV")
        print("7. View Grouped Contacts")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            category = input("Category (Family/Work/etc.): ")
            add_contact(contacts, name, phone, email, category)
            save_contacts(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            results = search_contacts(contacts, keyword)
            view_contacts(results)

        elif choice == "4":
            name = input("Enter name to edit: ")
            new_name = input("New name (or press Enter to skip): ") or None
            new_phone = input("New phone (or press Enter to skip): ") or None
            new_email = input("New email (or press Enter to skip): ") or None
            new_category = input("New category (or press Enter to skip): ") or None
            edit_contact(contacts, name, new_name, new_phone, new_email, new_category)
            save_contacts(contacts)

        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
            save_contacts(contacts)

        elif choice == "6":
            export_to_csv(contacts)

        elif choice == "7":
            grouped = group_contacts(contacts)
            for category, group in grouped.items():
                print(f"\nCategory: {category}")
                view_contacts(group)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
