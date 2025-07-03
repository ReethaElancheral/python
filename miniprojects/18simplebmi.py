## 18. Simple BMI Calculator

# - Ask for weight (kg) and height (m).
# - Calculate BMI and print with a message.
# - Show the type of BMI variable.

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in centimeters: "))

height_m = height_cm / 100


bmi = weight / (height_m ** 2)

print(f"Your BMI is: {bmi:.2f}")

print("Type of BMI variable:", type(bmi))

