# 🧩 16. Quiz App

# Topics Covered: function nesting, return, score tracking
# Requirements:
# Outer function calls inner quiz function
# Return total score
# Use conditionals to verify correct answers

def quiz_app():
    score = 0

    def quiz():
        nonlocal score  

        questions = [
            ("What is the capital of France?", "Paris"),
            ("2 + 2 = ?", "4"),
            ("Python is a programming language? (yes/no)", "yes"),
        ]

        for question, correct_answer in questions:
            answer = input(question + " ").strip().lower()
            if answer == correct_answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Wrong!")

    quiz()
    return score

total_score = quiz_app()
print(f"Quiz completed. Your total score is {total_score}/{3}")
