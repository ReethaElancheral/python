# 2. User Registration Form Validator

# Use Case: Collect name, email, age, and password. 
# Exception Handling Goals:
# Raise ValueError if age is not integer or < 13
# Raise TypeError if name/email is not string
# Raise custom PasswordTooWeakError
# Catch all and log invalid fields
# Use assert for pre-checks

import logging

# Setup logging
logging.basicConfig(filename="registration_errors.log", level=logging.ERROR)

# Custom Exception
class PasswordTooWeakError(Exception):
    pass

def register_user():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age_input = input("Enter age: ")
        password = input("Enter password: ")

        # Assertions for pre-checks
        assert name != "", "Name cannot be empty"
        assert email != "", "Email cannot be empty"

        # Type checks
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")

        # Age check
        try:
            age = int(age_input)
        except ValueError:
            raise ValueError("Age must be an integer.")

        if age < 13:
            raise ValueError("You must be at least 13 years old to register.")

      
        if len(password) < 6 or password.isnumeric() or password.isalpha():
            raise PasswordTooWeakError("Password must be at least 6 characters and contain letters & numbers.")

        print("✅ Registration successful!")

    except (TypeError, ValueError, PasswordTooWeakError, AssertionError) as e:
        logging.error(f"Invalid field: {e}", exc_info=True)
        print(f"❌ Registration failed: {e}")
    except Exception as e:
        logging.error("Unexpected error", exc_info=True)
        print(f"❌ Unexpected error: {e}")

# Run it
if __name__ == "__main__":
    register_user()
