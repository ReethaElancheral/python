# 6. Login Authentication System

# Objective: Validate user login.
# Requirements:
# Predefined username and password.
# Use input() to get credentials.
# Use if-else for validation.
# Use identity operators (is, is not) to compare input and stored credentials.


stored_username = "admin"
stored_password = "pass123"

username = input("Enter username: ")
password = input("Enter password: ")

if username is stored_username and password is stored_password:
    print("✅ Login successful!")
else:
    print("❌ Login failed. Invalid credentials.")
