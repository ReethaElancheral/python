# 11. Odd or Even Number Detector

# Objective: Check if number is odd or even.
# Requirements:
# Input: number.
# Use modulus operator %.
# Use if-else and formatted result.


num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
