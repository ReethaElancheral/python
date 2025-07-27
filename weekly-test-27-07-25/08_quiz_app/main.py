from quiz.question_bank import load_questions
from quiz.quiz_manager import QuizManager

def main():
    print("Welcome to the Quiz Application!")
    questions = load_questions("questions.json")

    while True:
        print("\nSelect difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. All")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            diff = "easy"
        elif choice == "2":
            diff = "medium"
        elif choice == "3":
            diff = "hard"
        elif choice == "4":
            diff = None
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        quiz = QuizManager(questions, time_per_question=15)
        quiz.run_quiz(difficulty=diff)

if __name__ == "__main__":
    main()
