from questions import questions
from evaluate import evaluate

def run_quiz():
    answers = [input(q[0] + " ") for q in questions]
    score = evaluate(questions, answers)
    print(f"You scored {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
