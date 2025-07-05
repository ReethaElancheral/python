## 12. Simple Quiz

# - Ask the user three simple questions (input).
# - Store answers in a list.
# - Print the answers and types of each.

answer1 = input("What is the capital of France? ")
answer2 = int(input("What is 2 + 2? "))
answer3 = input("What color is the sky? ")

answers = [answer1, answer2, answer3]

print(*answers, sep=",")

print("Answer 1:", answers[0], "Type:", type(answers[0]))
print("Answer 2:", answers[1], "Type:", type(answers[1]))
print("Answer 3:", answers[2], "Type:", type(answers[2]))
