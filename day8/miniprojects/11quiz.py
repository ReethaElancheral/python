# 11. Quiz Answer Tracker

# Description: Store and evaluate quiz answers.
# User inputs stored in a list.
# Compare with correct answers using index.
# Count total correct/incorrect answers.

correct_answers = ['a', 'c', 'b', 'd', 'a']

user_answers = []

print("Answer the following 5 questions (options: a, b, c, d):")

for i in range(len(correct_answers)):
    ans = input(f"Q{i+1}: Your answer: ").lower()

    if ans in ['a', 'b', 'c', 'd']:
        user_answers.append(ans)
    else:
        print("Invalid option, recorded as incorrect.")
        user_answers.append('')  

correct_count = 0
incorrect_count = 0

for i in range(len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        correct_count += 1
        result = "Correct"
    else:
        incorrect_count += 1
        result = "Incorrect"
    print(f"Q{i+1}: Your answer: {user_answers[i]} | Correct answer: {correct_answers[i]} | {result}")

print(f"\nTotal Correct: {correct_count}")
print(f"Total Incorrect: {incorrect_count}")
