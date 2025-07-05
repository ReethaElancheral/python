# ✅ 3. Custom Multiplication Table Generator

# Objective: Generate a multiplication table for any number.
# Requirements:
# Input: any number.
# Use range(1, 11) in a for loop.
# Print num x i = result format.
# Use f-string for output.


num = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
