# 8. Simple Poll App

# Description: Take responses to a question and analyze results.
# Store answers in a list.
# Count how many voted "Yes" or "No".
# Remove incorrect inputs.



responses = []
num_votes = int(input("How many people will vote? "))

for i in range(num_votes):
    answer = input(f"Person {i+1}, do you like Python? (yes/no): ").lower()
    if answer == "yes" or answer == "no":
        responses.append(answer)
    else:
        print("Invalid response. Skipped.")

yes_count = responses.count("yes")
no_count = responses.count("no")

print("📊 Poll Results:")
print("Yes:", yes_count)
print("No:", no_count)
