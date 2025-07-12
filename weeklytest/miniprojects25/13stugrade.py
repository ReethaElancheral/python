# 13. Student Grade Calculator

# Concepts: functions, list, loop, strings.
# Take student name and subject marks.
# Calculate average, grade, and store in list.
# Loop to handle multiple students.

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def input_marks(num_subjects):
    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            mark = input(f"Enter mark for subject {i}: ").strip()
            if mark.isdigit() and 0 <= int(mark) <= 100:
                marks.append(int(mark))
                break
            else:
                print("Invalid input. Enter a number between 0 and 100.")
    return marks

students = []

num_subjects = 3  

while True:
    name = input("Enter student name (or type 'exit' to finish): ").strip()
    if name.lower() == "exit":
        break
    print(f"Enter marks for {num_subjects} subjects:")
    marks = input_marks(num_subjects)
    average = sum(marks) / num_subjects
    grade = calculate_grade(average)

    students.append({"name": name, "marks": marks, "average": average, "grade": grade})

print("\n=== Student Grades ===")
for s in students:
    marks_str = ', '.join(str(m) for m in s["marks"])
    print(f"{s['name']}: Marks: [{marks_str}], Average: {s['average']:.2f}, Grade: {s['grade']}")
