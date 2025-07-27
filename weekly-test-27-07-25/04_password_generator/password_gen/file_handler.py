from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
DATA_FILE = "passwords.enc"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def save_passwords(passwords):
    try:
        key = load_key()
    except FileNotFoundError:
        generate_key()
        key = load_key()

    fernet = Fernet(key)
    data = "\n".join(passwords).encode()
    encrypted = fernet.encrypt(data)

    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def load_passwords():
    key = load_key()
    fernet = Fernet(key)
    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
    return fernet.decrypt(encrypted).decode().splitlines()
