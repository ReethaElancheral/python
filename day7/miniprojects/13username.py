# 13. Username Creator

# Concepts: slicing, concatenation
# Input: full name
# Username = first 3 letters of first name + last 2 letters of last name
# Example: "John Smith" → "Johth"


full_name = input("Enter your full name (e.g. John Smith): ").strip()

parts = full_name.split()

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]

    username = first_name[:3] + last_name[-2:]

    print("Generated Username:", username)
else:
    print("Please enter both first and last names.")
