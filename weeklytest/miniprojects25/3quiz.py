# 3. Quiz Game with Score Tracking

# Concepts: functions, list of questions, strings, while.
# Load questions into a list of strings.
# Use a while loop to ask each question.
# Use functions to check answers and update score.
# Show final score and percentage.


questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
    {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
    {"question": "Who wrote 'Hamlet'?", "answer": "shakespeare"},
    {"question": "What is 5 x 6?", "answer": "30"}
]

score = 0

def ask_question(q, correct_answer):
    global score
    user_answer = input(q + " ").strip().lower()
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")


print("=== Welcome to the Quiz Game ===\n")
index = 0
while index < len(questions):
    current = questions[index]
    ask_question(current["question"], current["answer"])
    index += 1


total_questions = len(questions)
percentage = (score / total_questions) * 100

print("=== Quiz Complete ===")
print(f"Your Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")
