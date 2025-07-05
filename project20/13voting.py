# ✅ 13. Voting Eligibility Checker

# Objective: Check who can vote from a list.
# Requirements:
# Input list of ages.
# Use for loop and condition to print who is eligible (age ≥ 18).

ages_input = input("Enter ages separated by commas: ").split(',')

ages = [int(age.strip()) for age in ages_input]

print("\nVoting Eligibility:")
for i, age in enumerate(ages, start=1):
    if age >= 18:
        print(f"Person {i} (Age: {age}) is Eligible to vote.")
    else:
        print(f"Person {i} (Age: {age}) is Not eligible to vote.")
