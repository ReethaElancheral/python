# ✅ 9. Number Type Classifier

# Objective: Classify numbers into odd and even using for loop.
# Requirements:
# Input: a list of 10 numbers.
# Use for loop + if condition.
# Store odd and even in separate lists.
# Display both lists.

nums_input = input("Enter 10 numbers separated by spaces: ")

numbers = [int(num) for num in nums_input.split()]

odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
