# 🧩 18. Loan EMI Calculator

# Topics Covered: function with formulas, return, lambda
# Requirements:
# Input principal, rate, time
# Use EMI formula in function
# Bonus: use lambda to shorten logic

def emi_calculator(principal, annual_rate, time_years):

    monthly_rate = annual_rate / (12 * 100)
    months = time_years * 12


    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi


emi_lambda = lambda P, r, t: (P * (r / 1200) * (1 + r / 1200) ** (t * 12)) / ((1 + r / 1200) ** (t * 12) - 1)


P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (%): "))
T = float(input("Enter time in years: "))

emi_value = emi_calculator(P, R, T)
print(f"EMI calculated using function: ₹{emi_value:.2f}")

emi_value_lambda = emi_lambda(P, R, T)
print(f"EMI calculated using lambda: ₹{emi_value_lambda:.2f}")
