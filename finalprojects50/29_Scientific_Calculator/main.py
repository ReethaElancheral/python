


import math
import time
from functools import wraps

# Decorator to convert radians to degrees for trigonometric outputs
def radians_to_degrees(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return f"{math.degrees(result):.2f}°"
        return result
    return wrapper

def display_menu():
    print("\n--- Scientific Calculator ---")
    print("Available operations:")
    print("1. Add        (add x y)")
    print("2. Subtract   (sub x y)")
    print("3. Multiply   (mul x y)")
    print("4. Divide     (div x y)")
    print("5. Power      (pow x y)")
    print("6. Log        (log x)")
    print("7. Sqrt       (sqrt x)")
    print("8. Sin        (sin x)")
    print("9. Cos        (cos x)")
    print("10. Tan       (tan x)")
    print("Type 'exit' to quit")

@radians_to_degrees
def sin_func(x): return math.sin(math.radians(x))

@radians_to_degrees
def cos_func(x): return math.cos(math.radians(x))

@radians_to_degrees
def tan_func(x): return math.tan(math.radians(x))

def main():
    while True:
        display_menu()
        try:
            user_input = input("\nEnter command: ").strip().lower()
            if user_input == "exit":
                print("Goodbye!")
                break

            tokens = user_input.split()
            if not tokens:
                continue

            op = tokens[0]
            args = list(map(float, tokens[1:]))

            if op == "add" and len(args) == 2:
                print("Result:", args[0] + args[1])
            elif op == "sub" and len(args) == 2:
                print("Result:", args[0] - args[1])
            elif op == "mul" and len(args) == 2:
                print("Result:", args[0] * args[1])
            elif op == "div" and len(args) == 2:
                if args[1] == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                print("Result:", args[0] / args[1])
            elif op == "pow" and len(args) == 2:
                print("Result:", math.pow(args[0], args[1]))
            elif op == "log" and len(args) == 1:
                print("Result:", math.log10(args[0]))
            elif op == "sqrt" and len(args) == 1:
                print("Result:", math.sqrt(args[0]))
            elif op == "sin" and len(args) == 1:
                print("Result:", sin_func(args[0]))
            elif op == "cos" and len(args) == 1:
                print("Result:", cos_func(args[0]))
            elif op == "tan" and len(args) == 1:
                print("Result:", tan_func(args[0]))
            else:
                print("Invalid input or number of arguments.")
        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()
