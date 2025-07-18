def add_student_marks(gradebook, student_id, subjects_marks):
    key = (student_id,)

    if key in gradebook:
        print(f"Student {student_id} already added.")
        return

    gradebook[key] = subjects_marks
    print(f"Marks added for Student {student_id}.")

def calculate_average(subjects_marks):
    if not subjects_marks:
        return 0.0
    total = sum(subjects_marks.values())
    return round(total / len(subjects_marks), 2)

def display_grades(gradebook):
    if not gradebook:
        print("No student records found.")
        return

    print("\n--- Student Grades ---")
    for student_id, marks in gradebook.items():
        subjects = ', '.join(marks.keys())
        avg = calculate_average(marks)
        print(f"ID: {student_id[0]} | Subjects: {subjects} | Average: {avg}")
