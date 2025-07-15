# 18. College Course Manager

# Goal: Manage courses offered in a semester.
# Requirements:
# Each course: (course_id, name, (credits, faculty))
# Sort courses by credits.
# Use count() to see how many courses a faculty handles.
# Display using unpacked formatting.


courses = [
    ("CS101", "Introduction to Computer Science", (3, "Dr. Smith")),
    ("MATH201", "Calculus II", (4, "Dr. Johnson")),
    ("PHYS101", "Physics I", (3, "Dr. Lee")),
    ("CHEM101", "General Chemistry", (3, "Dr. Kim")),
    ("CS201", "Data Structures", (4, "Dr. Smith")),
    ("MATH101", "Calculus I", (3, "Dr. Johnson")),
    ("BIO101", "Biology I", (3, "Dr. Lee"))
]


def sort_courses_by_credits(courses):
    return sorted(courses, key=lambda x: x[2][0], reverse=True)


def count_courses_by_faculty(courses, faculty_name):
    return sum(1 for _, _, (_, faculty) in courses if faculty == faculty_name)


def display_courses(courses):
    print("\n📚 Course List (Sorted by Credits)")
    print("----------------------------------")
    for course_id, course_name, (credits, faculty) in courses:
        print(f"{course_id}: {course_name} | Credits: {credits} | Faculty: {faculty}")
    print("----------------------------------")


sorted_courses = sort_courses_by_credits(courses)


display_courses(sorted_courses)

faculty_name = "Dr. Smith"
course_count = count_courses_by_faculty(courses, faculty_name)
print(f"\n✅ {faculty_name} handles {course_count} courses.")
