# 🧩 12. Python Calculator

# Topics Covered: first-class functions, lambda, return
# Requirements:
# Define functions for +, –, ×, ÷
# Pass them as arguments to a calculator() function
# Choose operation dynamically


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator(operation, x, y):
    return operation(x, y)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


num1 = 10
num2 = 5

for symbol, func in operations.items():
    result = calculator(func, num1, num2)
    print(f"{num1} {symbol} {num2} = {result}")


user_op = input("Choose operation (+, -, *, /): ")
if user_op in operations:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"Result: {calculator(operations[user_op], x, y)}")
else:
    print("Invalid operation selected.")
