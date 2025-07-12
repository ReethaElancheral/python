# 18. Mini Email Formatter

# Concepts: strings, string methods, functions.
# Take name and domain from user.
# Generate formatted email.
# E.g., john.doe@example.com.

def format_email(name, domain):
  
    name = name.strip().lower()
    domain = domain.strip().lower()

    email_name = name.replace(" ", ".")

    email = f"{email_name}@{domain}"
    return email

full_name = input("Enter full name: ")
email_domain = input("Enter domain (e.g., example.com): ")

formatted_email = format_email(full_name, email_domain)
print(f"Formatted Email: {formatted_email}")
