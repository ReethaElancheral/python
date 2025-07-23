# Basic Exception Handling (1–10)

# 1. Divide two numbers, handle ZeroDivisionError and ValueError.

def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print(f"Result: {a / b}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

divide_numbers()

# 2. Take user input for age, raise error if input is non-numeric or negative.

def validate_age_input():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as ve:
        print(f" Invalid input: {ve}")
    else:
        print(f"✅ Your age is: {age}")

validate_age_input()


# 3. Open a file, handle FileNotFoundError.

def open_file_safely():
    try:
        filename = input("Enter filename to open: ")
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(" Error: File not found.")

open_file_safely()

# 4. Read from a closed file, handle ValueError.

def read_from_closed_file():
    try:
        f = open("example.txt", "w")
        f.close()  # Now the file is closed
        if f.closed:
            print("File is closed.")
        print(f.read())  # This will raise ValueError
    except ValueError as ve:
        print(f"❌ Error: {ve}")


read_from_closed_file()


# 5. Handle IndexError when accessing list items by user input index.

def access_list_item():
    items = ["apple", "banana", "cherry"]
    try:
        index = int(input("Enter index (0 to 2): "))
        print(f"Item at index {index}: {items[index]}")
    except IndexError:
        print(" Error: Index out of range.")
    except ValueError:
        print(" Error: Please enter a valid number.")

access_list_item()



# 6. Handle KeyError when accessing a dictionary with a missing key.

def access_dict_key():
    data = {"name": "Nisha", "city": "Doha"}
    try:
        key = input("Enter key to lookup: ")
        print(f"Value: {data[key]}")
    except KeyError:
        print("❌ Error: Key not found in dictionary.")

access_dict_key()


# 7. Ask user to enter a number, convert to int, catch ValueError.

def convert_input_to_int():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("❌ Error: Invalid number.")
    else:
        print(f"✅ You entered: {number}")

convert_input_to_int()


# 8. Catch TypeError when trying to add string and integer.

def catch_type_error():
    try:
        result = "Age: " + 25  
    except TypeError as te:
        print(f"❌ Type Error: {te}")
    else:
        print(f"✅ Result: {result}")

catch_type_error()

# 9.  Catch AttributeError by calling a non-existent method on an object.

def catch_attribute_error():
    try:
        num = 10
        num.append(5) 
    except AttributeError as ae:
        print(f"❌ Attribute Error: {ae}")

catch_attribute_error()

# 10. Handle NameError when accessing an undefined variable.
 

def handle_name_error():
    try:
        print(undefined_variable)
    except NameError as ne:
        print(f"❌ Name Error: {ne}")

handle_name_error()


# Multiple Except, Else, Finally Blocks (11–20)

# 11. Demonstrate try with else: divide numbers only if no exception.

def divide_with_else():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
    except ValueError:
        print("❌ Invalid input. Please enter integers.")
    else:
        try:
            result = a / b
        except ZeroDivisionError:
            print("❌ Cannot divide by zero.")
        else:
            print(f"✅ Result: {result}")

divide_with_else()

# 12. Demonstrate try with finally: print "Done" regardless of error.

def try_finally_done():
    try:
        num = int(input("Enter a number: "))
        print(f"✅ You entered: {num}")
    except ValueError:
        print("❌ Not a valid number.")
    finally:
        print("✅ Done.")

try_finally_done()



# 13. Use multiple except blocks to catch ValueError and ZeroDivisionError.

def multiple_except_blocks():
    try:
        x = int(input("Enter numerator: "))
        y = int(input("Enter denominator: "))
        print(f"Result: {x / y}")
    except ValueError:
        print("❌ Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")


multiple_except_blocks()

# 14. Show that finally runs even when exception is raised and not caught.

def uncaught_exception_finally():
    try:
        print("Attempting to open an undefined variable...")
        print(undefined_variable)  
    finally:
        print("✅ Finally block executed.")


uncaught_exception_finally()


# 15. Demonstrate combining else and finally together.

def else_and_finally_demo():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("❌ Invalid input.")
    else:
        print(f"✅ Valid number: {num}")
    finally:
        print("✅ Operation finished.")


else_and_finally_demo()

# 16. Handle exception in file reading and ensure file is closed using finally.

def read_file_with_finally():
    file = None
    try:
        file = open("sample.txt", "r")
        print(file.read())
    except FileNotFoundError:
        print("❌ File not found.")
    finally:
        if file:
            file.close()
            print("✅ File closed.")

read_file_with_finally()



# 17. Nested try-except blocks: one inside another.


def nested_try_blocks():
    try:
        x = int(input("Enter a number: "))
        try:
            result = 10 / x
        except ZeroDivisionError:
            print("❌ Inner: Cannot divide by zero.")
        else:
            print(f"✅ Inner Result: {result}")
    except ValueError:
        print("❌ Outer: Invalid input.")

nested_try_blocks()



# 18. Handle a situation where multiple types of exceptions might occur.

def multiple_exception_scenarios():
    try:
        num = int(input("Enter an integer: "))
        print("String" + num) 
    except ValueError:
        print("❌ Invalid integer.")
    except TypeError:
        print("❌ Type mismatch between string and integer.")

multiple_exception_scenarios()



# 19. Use except Exception as a generic fallback and explain it.

def generic_exception_catch():
    try:
        val = int("abc")  # ValueError
    except Exception as e:
        print(f"❌ Caught general exception: {type(e).__name__} — {e}")

generic_exception_catch()



# 20. Demonstrate incorrect nesting of try-except-finally and correct it.

def correct_try_except_finally():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("❌ Invalid input.")
    finally:
        print("✅ This will always run.")

# ❌ Incorrect nesting 
# try:
#     try:
#         ...
#     finally:
#         ...
# except:
#     ...  # This causes logical issues; better to have finally last.

correct_try_except_finally()


# Raise Statement (21–30)

# 21. Raise ValueError manually if user enters a negative number.

def check_positive_number():
    try:
        num = int(input("Enter a positive number: "))
        if num < 0:
            raise ValueError("Number must be positive.")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    else:
        print(f"✅ You entered: {num}")


check_positive_number()

# 22. Raise TypeError if function argument is not a string.

def process_string(text):
    if not isinstance(text, str):
        raise TypeError("Argument must be a string.")
    print(f"✅ Processing string: {text}")


process_string(5)

# 23. Create a function that only accepts positive integers, use raise.


def accept_positive_integer(n):
    if not isinstance(n, int):
        raise TypeError("Only integers allowed.")
    if n <= 0:
        raise ValueError("Only positive integers allowed.")
    print(f"✅ Valid input: {n}")

accept_positive_integer(-5)


# 24. Simulate a login system and raise exception if password is incorrect.

def login_system():
    correct_password = "python123"
    try:
        entered = input("Enter password: ")
        if entered != correct_password:
            raise PermissionError("Incorrect password.")
    except PermissionError as pe:
        print(f"❌ Login failed: {pe}")
    else:
        print("✅ Login successful.")

login_system()



# 25. Raise an error if a required key is missing from a dictionary.

def check_required_key(data, key):
    """
    Raises KeyError if the specified key is missing in the dictionary.
    """
    if key not in data:
        raise KeyError(f"Missing required key: '{key}'")
    print(f"✅ Key '{key}' exists with value: {data[key]}")

# === Example 1: Missing key ===
try:
    user_info = {"name": "Nisha", "city": "Doha"}
    check_required_key(user_info, "email")  # key not present
except KeyError as ke:
    print(f"❌ Error: {ke}")

# === Example 2: Existing key ===
try:
    check_required_key(user_info, "name")  # key present
except KeyError as ke:
    print(f"❌ Error: {ke}")




# 26. Raise a ZeroDivisionError with custom error message.


def custom_zero_division(x):
    if x == 0:
        raise ZeroDivisionError("Cannot divide by zero (custom message).")
    print(f"✅ 10 / {x} = {10 / x}")

custom_zero_division(0)


# 27. Use assert to raise error if number is not even.

def assert_even_number(n):
    assert n % 2 == 0, "Number is not even."
    print(f"✅ {n} is even.")


assert_even_number(3)

# 28. Validate email format and raise a ValueError if invalid.

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")
    print(f"✅ Valid email: {email}")

validate_email("nishareetha")


# 29. Raise an exception if list is empty before processing.

def process_list(items):
    if not items:
        raise ValueError("List is empty. Cannot process.")
    print(f"✅ List has {len(items)} items.")

process_list()



# 30. Raise error if file is empty before reading.

def read_non_empty_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if not content.strip():
                raise ValueError("File is empty.")
            print("✅ File content:")
            print(content)
    except FileNotFoundError:
        print("❌ File not found.")
    except ValueError as ve:
        print(f"❌ {ve}")

read_non_empty_file('text.txt')


# Custom/User-Defined Exceptions (31–40)

# 31. Create a custom exception NegativeNumberError and raise it.

# Define the custom exception
class NegativeNumberError(Exception):
    """Raised when a negative number is entered."""
    pass

# Use the custom exception
def validate_positive_number():
    try:
        num = int(input("Enter a positive number: "))
        if num < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
    except NegativeNumberError as ne:
        print(f"❌ Custom Error: {ne}")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    else:
        print(f"✅ Valid input: {num}")

validate_positive_number()



# 32. Define InvalidAgeError and use it in age-based logic.

class InvalidAgeError(Exception):
    """Raised when age is out of acceptable range."""
    pass

def validate_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            raise InvalidAgeError("Age must be between 0 and 120.")
    except InvalidAgeError as ia:
        print(f"❌ Age Error: {ia}")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    else:
        print(f"✅ Valid age: {age}")

validate_age()



# 33.  Build a banking app with InsufficientFundsError.

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass

def withdraw_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough balance to withdraw.")
    print(f"✅ Withdrawal successful. Remaining balance: ₹{balance - amount}")


try:
    withdraw_funds(1000, 1500)
except InsufficientFundsError as e:
    print(f"❌ {e}")



# 34. Create a grading app and raise GradeOutOfRangeError for marks > 100.

class GradeOutOfRangeError(Exception):
    """Raised when marks are out of the allowed range (0–100)."""
    pass

def grade_student(marks):
    if marks < 0 or marks > 100:
        raise GradeOutOfRangeError("Marks must be between 0 and 100.")
    print(f"✅ Grade recorded: {marks}")

# usage: 

try:
    grade_student(110)
except GradeOutOfRangeError as e:
    print(f"❌ {e}")




# 35. Raise UnauthorizedAccessError in a mock role-based system.

class UnauthorizedAccessError(Exception):
    """Raised when a user tries to access a restricted area."""
    pass

def access_admin_panel(role):
    if role != "admin":
        raise UnauthorizedAccessError("Access denied. Admins only.")
    print("✅ Welcome to the admin panel.")


try:
    access_admin_panel("guest")
except UnauthorizedAccessError as e:
    print(f"❌ {e}")




# 36. Use custom exception for invalid file format in a file uploader.

class InvalidFileFormatError(Exception):
    """Raised when uploaded file has unsupported format."""
    pass

def upload_file(filename):
    if not filename.endswith(".pdf"):
        raise InvalidFileFormatError("Only PDF files are supported.")
    print("✅ File uploaded successfully.")


try:
    upload_file("document.txt")
except InvalidFileFormatError as e:
    print(f"❌ {e}")



# 37. Create LoginAttemptsExceeded for user login system.

class LoginAttemptsExceeded(Exception):
    """Raised when login attempts exceed limit."""
    pass

def login_with_attempts(correct_password):
    attempts = 0
    while attempts < 3:
        pwd = input("Enter password: ")
        if pwd == correct_password:
            print("✅ Login successful.")
            return
        else:
            print("❌ Incorrect password.")
            attempts += 1
    raise LoginAttemptsExceeded("Maximum login attempts exceeded.")


try:
    login_with_attempts("secret123")
except LoginAttemptsExceeded as e:
    print(f"❌ {e}")



# 38. Create a class-level exception to enforce object state rules.

class InvalidStateError(Exception):
    """Raised when object is in an invalid state for an operation."""
    pass

class Car:
    def __init__(self):
        self.engine_on = False

    def drive(self):
        if not self.engine_on:
            raise InvalidStateError("Can't drive. Engine is off.")
        print("🚗 Driving...")

    def start_engine(self):
        self.engine_on = True
        print("🔑 Engine started.")

# usage 

my_car = Car()
try:
    my_car.drive()
except InvalidStateError as e:
    print(f"❌ {e}")



# 39. Create a file validation system that raises FileTooLargeError.

class FileTooLargeError(Exception):
    """Raised when file exceeds size limit."""
    pass

def validate_file_size(size_mb, max_mb=5):
    if size_mb > max_mb:
        raise FileTooLargeError(f"File too large: {size_mb}MB (max {max_mb}MB).")
    print("✅ File size is within limit.")

# Call the function
try:
    validate_file_size(8)
except FileTooLargeError as e:
    print(f"❌ {e}")




# 40. Build a temperature converter and raise exception if below absolute zero.

class BelowAbsoluteZeroError(Exception):
    """Raised when temperature is below absolute zero."""
    pass

def convert_to_kelvin(celsius):
    if celsius < -273.15:
        raise BelowAbsoluteZeroError("Temperature below absolute zero is not possible.")
    kelvin = celsius + 273.15
    print(f"✅ Temperature in Kelvin: {kelvin:.2f}K")

# Call the function
try:
    convert_to_kelvin(-300)
except BelowAbsoluteZeroError as e:
    print(f"❌ {e}")


# Exception Handling in Loops and Functions (41–45)

# 41. Ask user to enter 5 valid integers using a loop, handle bad inputs.

def get_five_integers():
    numbers = []
    while len(numbers) < 5:
        try:
            num = int(input(f"Enter integer {len(numbers)+1}/5: "))
            numbers.append(num)
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")
    print(f"✅ Collected integers: {numbers}")


get_five_integers()



# 42. Write a function that opens and reads file and handles any error.

def read_file_content(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("✅ File content:")
            print(content)
    except FileNotFoundError:
        print("❌ File not found.")
    except PermissionError:
        print("❌ Permission denied.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


read_file_content("example.txt")



# 43. Handle exception in recursive function (e.g., factorial).

def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0:
            return 1
        return n * factorial(n - 1)
    except ValueError as ve:
        print(f"❌ {ve}")


print("Factorial Result:", factorial(-5))




# 44. Inside a loop, catch and skip bad inputs instead of crashing.


def collect_positive_numbers():
    numbers = []
    for i in range(5):
        try:
            num = int(input(f"Enter number {i+1}: "))
            if num < 0:
                raise ValueError("Only positive numbers allowed.")
            numbers.append(num)
        except ValueError as ve:
            print(f"❌ Skipping input: {ve}")
    print(f"✅ Valid numbers: {numbers}")


collect_positive_numbers()


# 45. Demonstrate try-except inside a list comprehension (with filtering).

def parse_ints_with_try(str_list):
    result = []
    for item in str_list:
        try:
            result.append(int(item))
        except ValueError:
            continue
    print(f"✅ Cleaned integers: {result}")


parse_ints_with_try(['10', 'abc', '25', '5five', '30'])


# Real-Life Use Case Tasks (46–50)

# 46. Build a calculator that uses exception handling for all basic operations.

def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        else:
            raise ValueError("Invalid operation.")
        
        print(f"✅ Result: {result}")
    
    except ValueError as ve:
        print(f"❌ Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"❌ Math Error: {zde}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


calculator()



# 47. Build a file copy tool that handles all common file errors.

import shutil

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"✅ File copied from '{src}' to '{dst}'")
    except FileNotFoundError:
        print("❌ Source file not found.")
    except PermissionError:
        print("❌ Permission denied.")
    except Exception as e:
        print(f"❌ Error: {e}")


copy_file("source.txt", "destination.txt")



# 48. Build a user registration form that validates all fields and raises exceptions.

class InvalidEmailError(Exception): pass
class WeakPasswordError(Exception): pass

def register_user():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if "@" not in email or "." not in email:
            raise InvalidEmailError("Email format is invalid.")
        if len(password) < 6:
            raise WeakPasswordError("Password is too weak.")
        
        print("✅ Registration successful!")
    
    except InvalidEmailError as iee:
        print(f"❌ {iee}")
    except WeakPasswordError as wpe:
        print(f"❌ {wpe}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


register_user()



# 49. Create an app that logs all exceptions to a file (using logging).

import logging

# Configure logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

def risky_operation():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"✅ Result: {result}")
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        print("❌ An error occurred. Check error_log.txt")


risky_operation()



# 50. Simulate a payment gateway that handles all input and system errors gracefully.

def payment_gateway():
    try:
        name = input("Enter your name: ")
        amount = float(input("Enter amount to pay (INR): "))
        method = input("Payment method (card/upi/wallet): ")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if method not in ["card", "upi", "wallet"]:
            raise ValueError("Invalid payment method selected.")
        
        print(f"✅ Payment of ₹{amount:.2f} by {method} successful. Thank you, {name}!")

    except ValueError as ve:
        print(f"❌ Input Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


payment_gateway()
