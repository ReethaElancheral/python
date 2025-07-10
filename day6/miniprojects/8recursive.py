# 🧩 8. Recursive Factorial & Fibonacci Generator

# Topics Covered: recursion, return, if-else
# Requirements:
# One function to generate factorial using recursion
# Another to return nth Fibonacci number
# Show both in one script

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = 5
print(f"Factorial of {num} is {factorial(num)}")

fib_n = 7
print(f"{fib_n}th Fibonacci number is {fibonacci(fib_n)}")  
