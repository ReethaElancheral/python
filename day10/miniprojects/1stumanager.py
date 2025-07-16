# 1. Student Marks Manager

# Description: Manage marks for students across different subjects.
# Requirements:
# - Dictionary format: {student_name: {subject: mark}}
# - Add new students and subjects
# - Update marks using nested access
# - Remove student or subject
# - List all students and their average marks
# - Identify topper by comparing total marks
# - Use .get() to handle missing data
# - Apply dictionary comprehension to list passed students (avg > 50)



marks = {}

def add_student(student):
    marks.setdefault(student, {})

def add_or_update_mark(student, subject, mark):
    marks.setdefault(student, {})[subject] = mark

def remove_student(student):
    marks.pop(student, None)

def remove_subject(student, subject):
    if student in marks:
        marks[student].pop(subject, None)

def list_averages():
    for student, subs in marks.items():
        avg = sum(subs.values()) / len(subs) if subs else 0
        print(f"{student}: average = {avg:.2f}")

def find_topper():
    totals = {s: sum(v.values()) for s, v in marks.items()}
    return max(totals, key=totals.get, default=None)

def passed_students(threshold=50):
    return {s: avg for s, avg in ((stu, sum(v.values())/len(v)) for stu, v in marks.items())
            if avg > threshold}


add_student("Alice")
add_or_update_mark("Alice", "math", 75)
add_or_update_mark("Alice", "physics", 85)
add_or_update_mark("Bob", "math", 45)
add_or_update_mark("Bob", "chemistry", 55)
remove_subject("Bob", "chemistry")
add_student("Cara")

list_averages()
print("Topper:", find_topper())
print("Passed students:", passed_students())
