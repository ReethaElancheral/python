from exam.exam_creator import add_question, list_questions, list_topics

def main():
    question_bank = {}  
    topics = set()      

    while True:
        print("\nOnline Exam Creator")
        print("1. Add Question")
        print("2. View All Questions")
        print("3. View Topics")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            qid = input("Enter Question ID: ").strip()
            question_text = input("Enter the question: ").strip()
            options = [
                input("Option 1: "),
                input("Option 2: "),
                input("Option 3: "),
                input("Option 4: "),
            ]
            answer = input("Enter the correct option (e.g., 2): ").strip()
            topic = input("Enter topic: ").strip()

            add_question(question_bank, topics, (qid,), question_text, options, answer, topic)

        elif choice == "2":
            list_questions(question_bank)

        elif choice == "3":
            list_topics(topics)

        elif choice == "4":
            print("Exiting Exam Creator.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
