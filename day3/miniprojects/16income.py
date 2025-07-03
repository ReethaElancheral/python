# 16. Age and Income-Based Loan Checker

# Objective: Decide loan eligibility.
# Requirements:
# Input: age, income.
# Use if-elif-else:
# age < 21: Not eligible
# income < 20000: Not eligible
# else: Eligible
# Use logical operators and formatted output.

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))

if age < 21:
    eligibility = "Not eligible (Age below 21)"
elif income < 20000:
    eligibility = "Not eligible (Income below 20000)"
else:
    eligibility = "Eligible for loan"

print(f"\nLoan Eligibility Status: {eligibility}")
