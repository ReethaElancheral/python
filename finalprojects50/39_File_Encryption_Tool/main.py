import os
from cryptography.fernet import Fernet, InvalidToken
from functools import wraps

KEY_FILE = "secret.key"

def log_encryptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        filepath = args[1] if len(args) > 1 else kwargs.get('filepath', 'Unknown')
        operation = func.__name__
        print(f"[LOG] Operation: {operation} on file: {filepath}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error during {operation}: {e}")
            raise
    return wrapper

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = self.load_key()
        else:
            self.key = key
        self.fernet = Fernet(self.key)

    @staticmethod
    def generate_key():
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print(f"Encryption key generated and saved to {KEY_FILE}")
        return key

    @staticmethod
    def load_key():
        if not os.path.exists(KEY_FILE):
            print(f"Key file '{KEY_FILE}' not found. Generating new key.")
            return Cipher.generate_key()
        with open(KEY_FILE, "rb") as f:
            return f.read()

    @log_encryptions
    def encrypt_file(self, filepath):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist.")

        with open(filepath, "rb") as file:
            data = file.read()
        encrypted = self.fernet.encrypt(data)
        with open(filepath, "wb") as file:
            file.write(encrypted)
        print(f"File '{filepath}' encrypted successfully.")

    @log_encryptions
    def decrypt_file(self, filepath):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist.")

        with open(filepath, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted = self.fernet.decrypt(encrypted_data)
        except InvalidToken:
            raise ValueError("Invalid encryption key or corrupted file.")
        with open(filepath, "wb") as file:
            file.write(decrypted)
        print(f"File '{filepath}' decrypted successfully.")

def main():
    print("File Encryption Tool")
    print("---------------------")
    print("1. Generate new encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Exit")

    cipher = None

    while True:
        choice = input("Select an option (1-4): ").strip()
        if choice == '1':
            Cipher.generate_key()
            cipher = None  # Reset cipher so user can reload key
        elif choice in ['2', '3']:
            if cipher is None:
                try:
                    cipher = Cipher()
                except Exception as e:
                    print(f"Failed to load key: {e}")
                    continue
            filepath = input("Enter file path: ").strip()
            try:
                if choice == '2':
                    cipher.encrypt_file(filepath)
                else:
                    cipher.decrypt_file(filepath)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option, please select 1-4.")

if __name__ == "__main__":
    main()

