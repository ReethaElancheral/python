# ✅ 12. Even Number Skipper

# Objective: Print numbers from 1 to 10, skip even numbers.
# Requirements:
# Use for loop with range().
# Use continue to skip even numbers.


for num in range(1, 11):
    if num % 2 == 0:
        continue 
    print(num)
