# 1. Personal Contact Manager 

# Objective: Store and manage contacts (name, phone, email). 
# Requirements: 
#  Use OOP (class Contact with attributes). 
#  Store contacts in a dictionary (key: name, value: Contact object). 
#  File Handling: Save/load contacts to/from a JSON file. 
#  Exception Handling: Validate phone/email format. 
#  Functions: Add, delete, search, update contacts. 
#  String Operations: Format contact display. 
#  Loops & Conditionals: Menu-driven interface. 
#  Modules: Use json for file operations. 
#  Decorator: Log function calls (e.g., @log_actions). 
#  Generator: Yield contacts one by one when searching. 



from contact_manager.manager import ContactManager

def main():
    manager = ContactManager()

    while True:
        print("\n📇 Personal Contact Manager")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. View All Contacts")
        print("6. Save & Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                name = input("Enter name: ").strip()
                phone = input("Enter phone (10 digits): ").strip()
                email = input("Enter email: ").strip()
                manager.add_contact(name, phone, email)

            elif choice == '2':
                name = input("Enter name to delete: ").strip()
                manager.delete_contact(name)

            elif choice == '3':
                name = input("Enter name to update: ").strip()
                phone = input("Enter new phone (or press Enter to skip): ").strip()
                email = input("Enter new email (or press Enter to skip): ").strip()
                manager.update_contact(name, phone or None, email or None)

            elif choice == '4':
                keyword = input("Enter name keyword to search: ").strip()
                manager.search_contact(keyword)

            elif choice == '5':
                manager.display_all()

            elif choice == '6':
                manager.save_contacts()
                print("Contacts saved. Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
