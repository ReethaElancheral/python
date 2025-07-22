from studentmarks.operations import add_student, view_records, show_summary
from studentmarks.display import show_menu

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            marks = input("Enter marks (out of 100): ")
            add_student(name, roll, marks)
        elif choice == "2":
            view_records()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Exiting Student Marks Recorder.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
