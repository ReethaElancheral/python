# 5. Login Attempt 

# Use Case: Allow user to attempt login max 3 times. 
# Exception Handling Goals:
# Raise custom LoginFailedError after 3 failed attempts
# Catch and handle input errors
# Log exception with timestamp for each failed attempt

import logging
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename="login_attempts.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

# Custom exception
class LoginFailedError(Exception):
    pass

# Dummy credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if not isinstance(username, str) or not isinstance(password, str):
                raise TypeError("Username and password must be strings.")

            if username == VALID_USERNAME and password == VALID_PASSWORD:
                print("✅ Login successful!")
                return

            else:
                attempts += 1
                raise ValueError("Incorrect credentials.")

        except (TypeError, ValueError) as e:
            logging.error(f"Login attempt {attempts}: {e}")
            print(f"❌ Attempt {attempts} failed. Reason: {e}")

        if attempts == max_attempts:
            try:
                raise LoginFailedError("Maximum login attempts exceeded.")
            except LoginFailedError as le:
                logging.error(le)
                print(f"🚫 {le}")


if __name__ == "__main__":
    login()
