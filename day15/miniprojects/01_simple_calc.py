import logging

# Setup logging
logging.basicConfig(filename="calculator_errors.log", level=logging.ERROR)

# Custom Exception
class InvalidOperationError(Exception):
    pass

def smart_calculator():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        operator = input("Enter operation (+, -, *, /, %): ")

        # Try converting inputs
        a = float(a)
        b = float(b)

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        elif operator == '%':
            if b == 0:
                raise ZeroDivisionError("Cannot perform modulo by zero.")
            result = a % b
        else:
            raise InvalidOperationError(f"'{operator}' is not a valid operation.")

    except ValueError:
        logging.error("Non-numeric input provided", exc_info=True)
        print("❌ Please enter valid numbers only.")
    except ZeroDivisionError as zde:
        logging.error("Division by zero", exc_info=True)
        print(f"❌ {zde}")
    except InvalidOperationError as ioe:
        logging.error("Invalid operation", exc_info=True)
        print(f"❌ {ioe}")
    except Exception as e:
        logging.error("Unexpected error", exc_info=True)
        print(f"❌ Unexpected error: {e}")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("📝 Calculation attempt complete.")


if __name__ == "__main__":
    smart_calculator()
