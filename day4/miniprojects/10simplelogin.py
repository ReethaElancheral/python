# ✅ 10. Simple Login Attempt Counter

# Objective: Allow a user only 3 attempts to log in.
# Requirements:
# Use a for loop with range(3).
# Ask for username and password.
# Use if to check; if correct, break loop.
# If 3 wrong attempts, print “Account Locked”.

correct_username = "admin"
correct_password = "pass123"

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print(f"Incorrect credentials. Attempts left: {2 - attempt}")
else:
    print("Account Locked")
