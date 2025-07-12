# 5. Password Strength Checker

# Concepts: strings, functions, while loop.
# Ask for password repeatedly until it meets criteria.
# Must include lowercase, uppercase, digit, and symbol.
# Use any() and string methods.
# Function to evaluate and return strength status.



def is_strong(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    return has_lower and has_upper and has_digit and has_symbol


while True:
    pwd = input("Enter a strong password: ")
    if is_strong(pwd):
        print("Password is strong ✅")
        break
    else:
        print("Password must include at least one lowercase, one uppercase, one digit, and one symbol.\n")
