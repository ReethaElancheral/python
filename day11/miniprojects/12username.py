# 12. Username Suggestion System

# Goal: Suggest new usernames without duplicates.
# Requirements:
# - Store taken usernames in a set.
# - Check new suggestions with in.
# - Keep only valid and unique suggestions.
# Concepts Covered: Membership, add(), discard().

# Set of already taken usernames
taken_usernames = {"alice123", "bob_the_builder", "charlie_88"}

# Function to suggest a new username
def suggest_username(username):
    if username in taken_usernames:
        print(f"Username '{username}' is already taken.")
    else:
        taken_usernames.add(username)
        print(f"Username '{username}' has been successfully added.")


suggest_username("alice123")  
suggest_username("david_smith") 
suggest_username("eve_2025")  

# Display all taken usernames
print("Taken usernames:", taken_usernames)
