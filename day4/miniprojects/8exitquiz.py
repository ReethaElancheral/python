# ✅ 8. Early Exit Quiz

# Objective: Exit the quiz if the wrong answer is given using break.
# Requirements:
# Ask 5 simple questions.
# If wrong answer is given, exit loop and display "Game Over".
# If completed, show “Quiz Completed”.

questions = [
    ("What is 2 + 2? ", "4"),
    ("What is the capital of France? ", "Paris"),
    ("What color do you get by mixing red and white? ", "Pink"),
    ("What is the opposite of hot? ", "Cold"),
    ("How many days are there in a week? ", "7")
]

for i, (question, answer) in enumerate(questions, start=1):
    user_answer = input(f"Q{i}: {question}")
    if user_answer.strip().lower() != answer.lower():
        print("Game Over")
        break
else:
  
    print("Quiz Completed")
