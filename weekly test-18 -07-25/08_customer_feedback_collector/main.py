from feedback.feedback_handler import add_feedback, display_feedback

def main():
    feedback_db = {}

    while True:
        print("\n=== Customer Feedback Collector ===")
        print("1. Submit Feedback")
        print("2. View All Feedback")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            customer_id = input("Enter Customer ID: ").strip()
            feedback_text = input("Enter feedback: ").strip()
            add_feedback(feedback_db, customer_id, feedback_text)

        elif choice == '2':
            display_feedback(feedback_db)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
