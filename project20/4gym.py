# ✅ 4. Gym Membership Checker

# Objective: Check if a person is eligible for gym offers.
# Requirements:
# Variables: name, age, BMI.
# Use if:
# If age > 18 and BMI < 25 → Eligible
# Else → Not Eligible
# Display formatted output.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))


print("\n🏋️‍♀️ Gym Membership Eligibility")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"BMI  : {bmi}")

if age > 18 and bmi < 25:
    print("✅ Status: Eligible for special gym offers!")
else:
    print("❌ Status: Not eligible for gym offers.")
