# 11. Quiz Game App

# Use Case: User answers multiple-choice questions. 
# Exception Handling Goals:
# Catch wrong input types
# Use raise for answer outside A/B/C/D
# Track and log all exceptions
# Use loop + exception for multiple questions

import logging

# Setup logging
logging.basicConfig(filename="quiz_game_errors.log", level=logging.ERROR)

# Custom exception for invalid answers
class InvalidAnswerError(Exception):
    pass

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

def quiz_game():
    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        for option in q['options']:
            print(option)

        while True:
            try:
                user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
                if user_answer not in ['A', 'B', 'C', 'D']:
                    raise InvalidAnswerError("Answer must be one of A, B, C, or D.")
            except InvalidAnswerError as iae:
                logging.error(f"Invalid answer input at Q{idx}: {iae}")
                print(f"❌ {iae} Please try again.")
            else:
                if user_answer == q['answer']:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Incorrect! The correct answer was {q['answer']}.")
                break

    print(f"\n🎉 Quiz Completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()
