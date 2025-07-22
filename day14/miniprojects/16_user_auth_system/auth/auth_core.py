import hashlib
import os
from datetime import datetime

USERS_FILE = "users.txt"
LOG_FILE = "login_attempts.log"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, hashed_password):
    with open(USERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed_password}\n")

def user_exists(username):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.split(",")[0] == username:
                return True
    return False

def verify_user(username, password):
    hashed = hash_password(password)
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            user, pwd = line.strip().split(",", 1)
            if user == username and pwd == hashed:
                return True
    return False

def log_attempt(username, success):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILURE"
        f.write(f"[{time_str}] Login attempt by '{username}': {status}\n")

def signup():
    username = input("Choose username: ").strip()
    if user_exists(username):
        print("Username already exists.")
        return
    password = input("Choose password: ").strip()
    hashed_pwd = hash_password(password)
    save_user(username, hashed_pwd)
    print("✅ Signup successful.")

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if verify_user(username, password):
        print("✅ Login successful.")
        log_attempt(username, True)
    else:
        print("❌ Invalid credentials.")
        log_attempt(username, False)
