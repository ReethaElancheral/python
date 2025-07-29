# contact_manager/contact.py

import re

class Contact:
    def __init__(self, name, phone, email):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

    @staticmethod
    def validate_phone(phone):
        return re.fullmatch(r'\d{10}', phone)

    @staticmethod
    def validate_email(email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["email"])
