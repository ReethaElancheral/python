# 8. Simple Calculator App

# Objective: Perform operations based on user choice.
# Requirements:
# Input: two numbers and operation (+, -, *, /, %, **).
# Use if-elif-else to perform arithmetic operation.
# Use formatted output.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /, %, **): ")

if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "%":
    result = num1 % num2
    print(f"Result: {num1} % {num2} = {result}")
elif operation == "**":
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")
else:
    print("Invalid operation. Please enter one of +, -, *, /, %, **")
