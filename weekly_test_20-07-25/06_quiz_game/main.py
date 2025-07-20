

import random
from quiz.questions import questions
from quiz.utils import check_answer


score = 0
topics = set()

def ask_question(q):
    global score
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    user = input("Your answer (A/B/C/D): ").strip().upper()
    if user == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. Correct answer is: {q['answer']}")
    topics.add(q["topic"])

def main():
    print("🎮 Welcome to the Quiz Game!\n")

    random.shuffle(questions)
    for q in questions:
        ask_question(q)

    print(f"\n🎯 Final Score: {score}/{len(questions)}")
    print(f"📚 Topics Covered: {', '.join(topics)}")

if __name__ == "__main__":
    main()
