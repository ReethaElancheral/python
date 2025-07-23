# 20. Secure Password Generator

# Use Case: Generate strong password from user specs. 
# Exception Handling Goals:
# Raise WeakPasswordCriteriaError if specs weak
# Handle user input issues
# Use assert for length validation
# try-else-finally to wrap generation 
 
import random
import string

# Custom Exception
class WeakPasswordCriteriaError(Exception):
    pass

def generate_password(length, use_upper, use_digits, use_special):
    
    if length < 8:
        raise WeakPasswordCriteriaError("Password length must be at least 8 characters.")

    if not (use_upper or use_digits or use_special):
        raise WeakPasswordCriteriaError("At least one of uppercase, digits, or special characters must be selected.")

    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_generator():
    try:
        length_input = input("Enter desired password length (min 8): ")
        length = int(length_input)
        assert length >= 8, "Length must be at least 8."

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        pwd = generate_password(length, use_upper, use_digits, use_special)
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for length.")
    except AssertionError as ae:
        print(f"❌ {ae}")
    except WeakPasswordCriteriaError as wcpe:
        print(f"❌ Weak criteria: {wcpe}")
    else:
        print(f"✅ Generated Password: {pwd}")
    finally:
        print("📝 Password generation process completed.")

if __name__ == "__main__":
    password_generator()
