# 🧩 15. Contact Book

# Topics Covered: **kwargs, functions, global dictionary
# Requirements:
# Add new contact using **kwargs
# Return sorted contact list
# Search function to return contact details

contacts = {}

def add_contact(**kwargs):
    global contacts
 
    name = kwargs.get('name')
    if not name:
        print("Contact must have a name.")
        return
    contacts[name] = kwargs
    print(f"Contact '{name}' added.")


def get_sorted_contacts():
    global contacts
    return sorted(contacts.keys())


def search_contact(name):
    global contacts
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."

add_contact(name="Nisha", phone="1234567890", email="nisha@example.com")
add_contact(name="Geetha", phone="0987654321")
add_contact(name="Karthi", phone="5555555555", address="123 Main St")

print("Sorted contacts:", get_sorted_contacts())

print("Searching for Mannavan:", search_contact("Mannavan"))
print("Searching for Yazh:", search_contact("Yazh"))
