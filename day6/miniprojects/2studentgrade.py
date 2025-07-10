# 🧩 2. Student Grading System

# Topics Covered: function with parameters, return, recursion
# Requirements:
# Function to input marks for 5 subjects
# Return average and grade using conditional logic
# Use recursion for re-evaluation if marks < 35


def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    else:
        return 'D'

def evaluate_student():
    print("\nEnter marks for 5 subjects:")
    marks = []
    
    for i in range(5):
        mark = int(input(f"Subject {i+1} marks: "))
        marks.append(mark)
  
    if any(mark < 35 for mark in marks):
        print("❌ Failed in one or more subjects. Re-evaluation needed.")
        return evaluate_student()  

    average = sum(marks) / 5
    grade = get_grade(average)

    return average, grade


name = input("Enter student name: ")
average, grade = evaluate_student()
print(f"\n{name}'s Result:")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
