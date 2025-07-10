# 🧩 13. Voting Eligibility Checker

# Topics Covered: return, conditionals, input(), lambda
# Requirements:
# Accept age
# Return whether eligible or not
# Bonus: Use lambda to check age >= 18

is_eligible = lambda age: "Eligible to vote" if age >= 18 else "Not eligible to vote"

def check_voting_eligibility():
    age = int(input("Enter your age: "))
    result = is_eligible(age)
    return result


print(check_voting_eligibility())
