# 12. Driving License Eligibility System
# Objective: Check eligibility based on age and documents.
# Requirements:
# Input: age, has_aadhar (yes/no).
# Use if and nested if to validate.
# Use logical, identity, and assignment operators.

age = int(input("Enter your age: "))
has_aadhar = input("Do you have an Aadhar card? (yes/no): ").lower()

if age >= 18:
    if has_aadhar == "yes":  
        eligible = True
    else:
        eligible = False
else:
    eligible = False


if eligible:
    print("You are eligible to apply for a driving license.")
else:
    print("You are NOT eligible to apply for a driving license.")

