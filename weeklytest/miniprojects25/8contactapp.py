# 8. Contact Book App

# Concepts: strings, functions, lists, while.
# Add new contact: name, phone, email.
# Store in list of lists.
# Search contact using string in operator.
# Loop for multiple options (search, delete, show all).

contacts = [] 


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if name and phone and email:
        contacts.append([name, phone, email])
        print(f"Contact '{name}' added.")
    else:
        print("All fields are required.")


def search_contact():
    keyword = input("Enter name or keyword to search: ").strip().lower()
    found = False
    print("\n=== Search Results ===")
    for c in contacts:
        if keyword in c[0].lower() or keyword in c[1] or keyword in c[2].lower():
            print(f"Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
            found = True
    if not found:
        print("No matching contact found.")


def delete_contact():
    name = input("Enter the name of contact to delete: ").strip().lower()
    for c in contacts:
        if c[0].lower() == name:
            contacts.remove(c)
            print(f"Contact '{c[0]}' deleted.")
            return
    print("Contact not found.")


def show_all():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\n=== All Contacts ===")
        for c in contacts:
            print(f"Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
        print()


while True:
    print("\n=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        show_all()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 5.")
