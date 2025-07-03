# 2. Electricity Bill Calculator

# Objective: Calculate the monthly bill based on units consumed.
# Requirements:
# Input: name, units.
# Use:
# if units ≤ 100 → ₹2/unit
# elif units ≤ 300 → ₹3/unit
# else → ₹5/unit
# Use arithmetic, assignment, and comparison operators.
# Display formatted bill using f-string.

name = input("Enter your name: ")
units = float(input("Enter units consumed: "))


if units <= 100:
    rate = 2
elif units>=100 or units<= 300:
    rate = 3
else:
    rate = 5

bill = units * rate  
print(f"{name}, your electricity bill for {units} units is ₹{bill:.2f}")

