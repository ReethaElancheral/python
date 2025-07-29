# passwordmanager/manager.py

import json
from passwordmanager.entry import PasswordEntry
from passwordmanager.security import AESCipher
from passwordmanager.decorators import logged_in

class PasswordManager:
    def __init__(self, key, filename="passwords.json"):
        self.filename = filename
        self.cipher = AESCipher(key)
        self.authenticated = False
        self.passwords = {}  # key: website, value: PasswordEntry
        self.compromised = set()
        self.load_passwords()

    def login(self):
        # For simplicity, assume login always succeeds if key works
        try:
            self.authenticated = True
            print("✅ Logged in successfully.")
        except Exception:
            print("❌ Invalid encryption key.")
            self.authenticated = False

    def load_passwords(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            for site, enc_data in data.items():
                username = self.cipher.decrypt(enc_data["username"])
                password = self.cipher.decrypt(enc_data["password"])
                self.passwords[site] = PasswordEntry(site, username, password)
            print(f"Loaded {len(self.passwords)} passwords.")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Failed to load passwords: {e}")

    @logged_in
    def save_passwords(self):
        data = {}
        for site, entry in self.passwords.items():
            data[site] = {
                "username": self.cipher.encrypt(entry.username),
                "password": self.cipher.encrypt(entry.password)
            }
        with open(self.filename, "w") as f:
            json.dump(data, f)
        print("✅ Passwords saved.")

    @logged_in
    def add_password(self, website, username, password):
        self.passwords[website] = PasswordEntry(website, username, password)
        print(f"✅ Password saved for {website}.")

    @logged_in
    def retrieve_password(self, website):
        entry = self.passwords.get(website)
        if entry:
            print(f"Website: {entry.website}\nUsername: {entry.username}\nPassword: {entry.password}")
        else:
            print("❌ No entry found for this website.")

    @logged_in
    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            print(f"✅ Password entry deleted for {website}.")
        else:
            print("❌ No entry found for this website.")

    @logged_in
    def track_compromised(self, password):
        self.compromised.add(password)
        print("Added to compromised passwords list.")

    @logged_in
    def weak_passwords_generator(self):
        # Define weak: length < 8 or no special chars
        def is_weak(pw):
            import string
            if len(pw) < 8:
                return True
            if not any(c in string.punctuation for c in pw):
                return True
            return False

        for entry in self.passwords.values():
            if is_weak(entry.password):
                yield entry
