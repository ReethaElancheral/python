# 7. Text-Based Calculator

# Concepts: functions, strings, lists.
# Ask user to input operation (add, subtract, etc.).
# Use functions for each operation.
# Store past results in a list.
# Loop until user exits.


results = []  

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Cannot divide by zero"


def get_number(prompt):
    num = input(prompt).strip()
    return float(num) if num.replace('.', '', 1).isdigit() else None


while True:
    print("\n=== Calculator Menu ===")
    print("Choose an operation: add, subtract, multiply, divide, history, exit")

    choice = input("Enter operation: ").strip().lower()

    if choice in ["add", "subtract", "multiply", "divide"]:
        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        if x is None or y is None:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == "add":
            result = add(x, y)
        elif choice == "subtract":
            result = subtract(x, y)
        elif choice == "multiply":
            result = multiply(x, y)
        elif choice == "divide":
            result = divide(x, y)

        print(f"Result: {result}")
        results.append(result)

    elif choice == "history":
        if not results:
            print("No previous results.")
        else:
            print("\n=== Calculation History ===")
            for i, r in enumerate(results, 1):
                print(f"{i}. {r}")
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid operation. Please try again.")
