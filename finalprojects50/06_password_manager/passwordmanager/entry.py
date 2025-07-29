# passwordmanager/entry.py

class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password  # Stored encrypted in file by manager

    def __str__(self):
        return f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.password}"
