# ✅ 3. Odd Number Printer

# Objective: Print only odd numbers from 1 to 20.
# Requirements:
# Use a while loop.
# Use continue to skip even numbers.
# Store the odd numbers in a list.

num = 1
odd_numbers = []

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue  

    odd_numbers.append(num)
    num += 1

print("Odd numbers from 1 to 20:", odd_numbers)
