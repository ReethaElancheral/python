# 14. Username Availability Checker

# Objective: Check if username is already taken.
# Requirements:
# Use a predefined list of usernames.
# Check membership using in, not in.
# Use if-else to display availability.


taken_usernames = ["admin", "user1", "guest", "reetha", "nisha"]

new_username = input("Enter desired username: ").lower()

if new_username in taken_usernames:
    print(f"Sorry, the username '{new_username}' is already taken.")
else:
    print(f"Great! The username '{new_username}' is available.")
