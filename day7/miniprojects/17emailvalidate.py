# 17. Email Validator

# Concepts: find(), slicing, indexing
# Check:
# Contains @ and .
# Domain should be "gmail.com"
# Username should be > 5 characters


email = input("Enter your email address: ").strip()

if "@" in email and "." in email:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index+1:]

    if domain == "gmail.com" and len(username) > 5:
        print("✅ Valid Gmail address.")
    else:
        if domain != "gmail.com":
            print("❌ Invalid domain. Only gmail.com is allowed.")
        if len(username) <= 5:
            print("❌ Username must be more than 5 characters.")
else:
    print("❌ Invalid email format. Missing '@' or '.'")
