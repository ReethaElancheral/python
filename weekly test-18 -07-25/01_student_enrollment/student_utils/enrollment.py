def add_student(students, student_id, name):
    if student_id not in students:
        students[student_id] = {"name": name, "courses": set()}
        print(f"Student '{name}' added.")
    else:
        print("Student ID already exists.")

def enroll_course(students, student_id, course, available_courses):
    if course not in available_courses:
        print(f"Course '{course}' is not available.")
        return
    if course in students[student_id]["courses"]:
        print(f"Student already enrolled in '{course}'.")
        return
    students[student_id]["courses"].add(course)
    print(f"Enrolled in '{course}' successfully.")
