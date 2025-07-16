# 7. Quiz Application

# Description: Store quiz questions and answers.
# Requirements:
# - Structure: {question: {"options": [...], "answer": ...}}
# - Loop through and accept user answers
# - Show result summary with score
# - Use nested dictionary and in check for validity
# - Track correct vs wrong answers using comprehension


quiz = {
    "What is the capital of France?": {
        "options": ["A) Berlin", "B) London", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    "2 + 2 = ?": {
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
    "Which language is this code in?": {
        "options": ["A) Java", "B) Python", "C) C#", "D) Ruby"],
        "answer": "B"
    }
}

def run_quiz(qdict):
    correct = {}
    total = len(qdict)

    for q, data in qdict.items():
        print("\n" + q)
        for opt in data["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        valid = ans in [o.split(")")[0] for o in data["options"]]
        if not valid:
            print("❌ Invalid choice, counted as wrong.")
            ans = None
        correct[q] = (ans == data["answer"])
    
  
    score = sum(1 for v in correct.values() if v)
    wrong = total - score

    print("\n📊 Quiz Results")
    print(f"You got {score}/{total} correct.")
    print(f"Correct: {score} | Wrong: {wrong}")

    
    incorrect = [q for q, v in correct.items() if not v]
    if incorrect:
        print("You got these wrong:")
        for q in incorrect:
            print(" -", q)


run_quiz(quiz)
