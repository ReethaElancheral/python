# 13. Salary Tax Deduction Calculator

# Objective: Calculate salary after tax.
# Requirements:
# Input: base salary.
# Use if-elif-else:
# <5L: 0% tax
# 5L–10L: 10%
# 10L: 20%
# Use arithmetic and assignment operators.

salary = float(input("Enter your base salary in lakhs: "))

if salary < 5:
    tax_rate = 0
elif 5 <= salary < 10:
    tax_rate = 0.10
else:  
    tax_rate = 0.20

tax_amount = salary * tax_rate
salary -= tax_amount  


print(f"\nBase Salary: ₹{salary + tax_amount:.2f} lakhs")
print(f"Tax Deducted: ₹{tax_amount:.2f} lakhs")
print(f"Salary after Tax: ₹{salary:.2f} lakhs")
