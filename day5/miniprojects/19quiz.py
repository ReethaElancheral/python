# ✅ 19. Quiz with Exit Option

# Objective: Ask user 5 questions and allow early exit.
# Requirements:
# Use a list of questions.
# Use while to iterate through them.
# Use break if user types "quit".
# Use else to show “Quiz complete” message.

questions = [
    "What is the capital of India? ",
    "What is 5 + 7? ",
    "What color do you get when you mix red and white? ",
    "Which planet is known as the Red Planet? ",
    "Who wrote 'Romeo and Juliet'? "
]

index = 0
total_questions = len(questions)

while index < total_questions:
    answer = input(f"Q{index + 1}: {questions[index]} (Type 'quit' to exit) ").strip().lower()
    
    if answer == "quit":
        print("Quiz exited early.")
        break
    
    index += 1
else:
    print("Quiz complete! Thanks for participating.")
