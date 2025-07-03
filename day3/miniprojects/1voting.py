# 🔥 1. Online Voting Eligibility Checker

# Objective: Check if a user is eligible to vote.
# Requirements:
# Input: name, age, citizenship status.
# Use if to check if age ≥ 18.
# Use and to check if citizenship is "Indian".
# Use f-string to display the result.
# Use type() to show data types.
# Use comparison and logical operators.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship status: ").strip()


print(f"Data types -> name: {type(name)}, age: {type(age)}, citizenship: {type(citizenship)}")


if age >= 18 and citizenship.lower() == "indian":
    print(f"{name}, you are eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote.")
