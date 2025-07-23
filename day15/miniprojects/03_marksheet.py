# 3. Student Marksheet Generator

# Use Case: Accept student name, subject-wise marks, calculate grade. 
# Exception Handling Goals:
# Raise error for negative marks
# Raise custom InvalidMarkError for marks > 100
# Catch and skip students with errors using loop-level exception
# Use try-except-else-finally block

# Custom exception
class InvalidMarkError(Exception):
    pass

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

def student_marksheet_generator():
    students = []

    try:
        total_students = int(input("Enter number of students: "))
    except ValueError:
        print("❌ Invalid number entered.")
        return

    for i in range(total_students):
        print(f"\n--- Student {i + 1} ---")
        try:
            name = input("Enter student name: ")
            subjects = ['Math', 'Science', 'English']
            marks = []

            for subject in subjects:
                mark = int(input(f"Enter marks for {subject}: "))
                if mark < 0:
                    raise ValueError(f"{subject} marks cannot be negative.")
                if mark > 100:
                    raise InvalidMarkError(f"{subject} marks cannot exceed 100.")
                marks.append(mark)

        except ValueError as ve:
            print(f"❌ Skipping student due to input error: {ve}")
        except InvalidMarkError as ime:
            print(f"❌ Skipping student due to invalid marks: {ime}")
        else:
            grade = calculate_grade(marks)
            students.append({'name': name, 'marks': marks, 'grade': grade})
            print(f"✅ {name}'s Grade: {grade}")
        finally:
            print("➡️ Student processing complete.")

    print("\n📋 Final Marksheet")
    for student in students:
        print(f"{student['name']} - Marks: {student['marks']}, Grade: {student['grade']}")


if __name__ == "__main__":
    student_marksheet_generator()
