# quiz/user/evaluate.py
import time
from quiz.admin.questions import load_questions

def run_quiz(num_questions=5):
    questions = load_questions(num_questions)
    answers = []
    start = time.time()
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"  {j}. {opt}")
        try:
            choice = int(input("Your answer: "))
        except ValueError:
            choice = None
        correct = (choice is not None and q['options'][choice-1] == q['answer'])
        answers.append(correct)
    elapsed = time.time() - start
    return answers, elapsed
