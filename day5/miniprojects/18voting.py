# ✅ 18. Voting Eligibility Checker

# Objective: Take 5 people’s age and check who can vote.
# Requirements:
# Use while loop for 5 iterations.
# Use if condition to check age ≥ 18.
# Count eligible voters.
# Use pass in future logic for address validation.

count = 0
eligible_voters = 0

while count < 5:
    age = int(input(f"Enter age of person {count + 1}: "))
    
    if age >= 18:
        print("Eligible to vote")
        eligible_voters += 1
        pass 
    else:
        print("Not eligible to vote")
    
    count += 1

print(f"Total eligible voters: {eligible_voters}")
