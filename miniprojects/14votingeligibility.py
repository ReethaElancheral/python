## 14. Voting Eligibility Checker

# - Ask for age (input).
# - Print whether the user is eligible to vote (18+).
# - Show the type of the age variable.

age = int(input("Enter your age: "))

eligibility = {
    True: "You are eligible to vote.",
    False: "You are not eligible to vote."
}

print(eligibility[age >= 18])

print("Type of age variable:", type(age))

