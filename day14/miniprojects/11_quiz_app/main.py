from quiz.quiz_core import load_questions, take_quiz, save_result
from quiz.display import show_banner

def main():
    show_banner()
    questions = load_questions("questions.csv")
    if not questions:
        print("❌ No questions found. Exiting.")
        return
    score = take_quiz(questions)
    name = input("Enter your name for the result: ").strip()
    save_result(name, score, len(questions))
    print(f"✅ Result saved for {name}.")

if __name__ == "__main__":
    main()
