# contact_manager/manager.py

import json
from contact_manager.contact import Contact
from contact_manager.utils import log_actions

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.contacts = {}
        self.filename = filename
        self.load_contacts()

    @log_actions
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        contact = Contact(name, phone, email)
        self.contacts[name] = contact
        print("Contact added successfully.")

    @log_actions
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    @log_actions
    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        contact = self.contacts[name]
        if phone:
            if not Contact.validate_phone(phone):
                raise ValueError("Invalid phone format.")
            contact.phone = phone
        if email:
            if not Contact.validate_email(email):
                raise ValueError("Invalid email format.")
            contact.email = email
        print("Contact updated.")

    @log_actions
    def search_contact(self, keyword):
        for contact in self.contact_generator():
            if keyword.lower() in contact.name.lower():
                print(contact)
                print("-" * 20)

    def contact_generator(self):
        for contact in self.contacts.values():
            yield contact

    def display_all(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contact_generator():
            print(contact)
            print("-" * 20)

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump({name: c.to_dict() for name, c in self.contacts.items()}, f, indent=4)

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.contacts = {name: Contact.from_dict(c) for name, c in data.items()}
        except FileNotFoundError:
            self.contacts = {}
        except json.JSONDecodeError:
            print("Failed to load contacts. JSON file might be corrupted.")
