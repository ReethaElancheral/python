
def add_student(roll_no, name, students):
    student_id = (roll_no, name)
    students.append({"id": student_id, "grades": {}})

def update_grade(roll_no, subject, grade, students):
    for student in students:
        if student["id"][0] == roll_no:
            student["grades"][subject] = grade
            return True
    return False

def get_all_subjects(students):
    subjects = set()
    for s in students:
        subjects.update(s["grades"].keys())
    return subjects
