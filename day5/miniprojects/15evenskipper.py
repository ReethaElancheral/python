# ✅ 15. Even Number Skipper

# Objective: Skip even numbers and print squares of odds.
# Requirements:
# Range: 1 to 20
# Use while loop and continue for even numbers.
# Print number and its square.

num = 1

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    print(f"{num} squared is {num ** 2}")
    num += 1
