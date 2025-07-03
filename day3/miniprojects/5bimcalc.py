# 5. BMI Calculator & Category Checker

# Objective: Calculate BMI and determine weight status.
# Requirements:
# Input: height, weight.
# Use BMI formula.
# Use if-elif for category:
# <18.5: Underweight
# 18.5–24.9: Normal
# 25–29.9: Overweight
# 30+: Obese
# Use arithmetic, comparison, and formatted output.


height_cm = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

height_m = height_cm / 100  

bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9 :
    category = "Normal"
elif bmi >=25 and bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Weight Category: {category}")

