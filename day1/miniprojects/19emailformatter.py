## 19. Email Formatter

# - Ask for user’s first and last name.
# - Generate a simple email (e.g., john.doe@example.com) using f-strings.
# - Print the email and its type.


first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()

email = f"{first_name}.{last_name}@example.com"


print(f"Generated email: {email}")
print("Type of email variable:", type(email))
