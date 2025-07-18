# quiz/main.py

import argparse
from quiz.user.evaluate import run_quiz
from quiz.user.score import calculate_score, display_score

def main():
    parser = argparse.ArgumentParser("Quiz App")
    parser.add_argument('--admin', action='store_true', help="Show sample questions")
    parser.add_argument('--num', type=int, default=5, help="Number of questions")
    args = parser.parse_args()

    if args.admin:
        from quiz.admin.questions import load_questions
        sample = load_questions(args.num)
        print("[Admin] Sample Questions:")
        for q in sample:
            print(" -", q['question'])
    else:
        results, elapsed = run_quiz(args.num)
        report = calculate_score(results, elapsed)
        display_score(report)

if __name__ == "__main__":
    main()
