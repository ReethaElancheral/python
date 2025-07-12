# 2. Student Score Tracker

# Description: Maintain student names and marks using lists and nested lists.
# Access and update specific student’s marks.
# Add or remove students.
# Use a nested list format: [['Ram', 85], ['Sam', 78]].
# Sort or analyze scores (highest/lowest).


students = [['Ram', 85], ['Sam', 78], ['Lina', 92]]

def show_students():
    if not students:
        print("No students in the list.")
        return
    print("\n📚 Student List:")
    for i, (name, score) in enumerate(students, 1):
        print(f"{i}. Name: {name}, Score: {score}")

def add_student():
    name = input("Enter student name: ")
    score = int(input(f"Enter {name}'s score: "))
    students.append([name, score])
    print(f"{name} added with score {score}.")

def remove_student():
    name = input("Enter name of student to remove: ")
    found = False
    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            print(f"{name} removed.")
            found = True
            break
    if not found:
        print(f"{name} not found.")

def update_score():
    name = input("Enter student name to update score: ")
    for student in students:
        if student[0].lower() == name.lower():
            new_score = int(input(f"Enter new score for {name}: "))
            student[1] = new_score
            print(f"{name}'s score updated to {new_score}.")
            return
    print(f"{name} not found.")

def view_student():
    name = input("Enter student name to view: ")
    for student in students:
        if student[0].lower() == name.lower():
            print(f"Name: {student[0]}, Score: {student[1]}")
            return
    print(f"{name} not found.")

def sort_by_score():
    sorted_list = sorted(students, key=lambda x: x[1], reverse=True)
    print("\n🎯 Students sorted by score (high to low):")
    for name, score in sorted_list:
        print(f"{name} - {score}")

def show_high_low():
    if not students:
        print("No student data available.")
        return
    scores = [student[1] for student in students]
    max_score = max(scores)
    min_score = min(scores)

    print("\n🏆 Highest Score(s):")
    for name, score in students:
        if score == max_score:
            print(f"{name} - {score}")

    print("\n📉 Lowest Score(s):")
    for name, score in students:
        if score == min_score:
            print(f"{name} - {score}")


while True:
    print("\n--- Student Score Tracker Menu ---")
    print("1. Show all students")
    print("2. Add a student")
    print("3. Remove a student")
    print("4. Update a student's score")
    print("5. View a specific student")
    print("6. Sort by score")
    print("7. Show highest and lowest scores")
    print("8. Exit")

    choice = input("Enter your choice (1–8): ")

    if choice == "1":
        show_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        update_score()
    elif choice == "5":
        view_student()
    elif choice == "6":
        sort_by_score()
    elif choice == "7":
        show_high_low()
    elif choice == "8":
        print("Exiting Student Tracker. 🎓")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
