from contacts.manager import create_contact, read_contacts, update_contact, delete_contact
from contacts.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_contact()
        elif choice == "2":
            read_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
