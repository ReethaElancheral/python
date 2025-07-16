# 17. College Course Registration

# Description: Manage student-course enrollments.
# Requirements:
# - {student_name: [courses]}
# - Add/drop course
# - Show all students in a course
# - Use in and not in for checks


enrollments = {
    "Alice": ["Math", "Science"],
    "Bob": ["History", "Math"],
    "Charlie": ["Science", "Art"],
}

def add_course(student_name, course_name):
    """Enroll a student in a new course."""
    if student_name in enrollments:
        if course_name not in enrollments[student_name]:
            enrollments[student_name].append(course_name)
            print(f"{student_name} has been enrolled in {course_name}.")
        else:
            print(f"{student_name} is already enrolled in {course_name}.")
    else:
        enrollments[student_name] = [course_name]
        print(f"New student {student_name} has been enrolled in {course_name}.")

def drop_course(student_name, course_name):
    """Remove a student from a course."""
    if student_name in enrollments:
        if course_name in enrollments[student_name]:
            enrollments[student_name].remove(course_name)
            print(f"{student_name} has been removed from {course_name}.")
        else:
            print(f"{student_name} is not enrolled in {course_name}.")
    else:
        print(f"{student_name} is not enrolled in any courses.")

def students_in_course(course_name):
    """List all students enrolled in a specific course."""
    students = [student for student, courses in enrollments.items() if course_name in courses]
    return students


add_course("Alice", "English")
drop_course("Bob", "Math")
print("Students enrolled in Science:", students_in_course("Science"))
