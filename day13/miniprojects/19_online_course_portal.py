# 19. Online Course Portal

# Concepts: Inheritance, Aggregation, Polymorphism
# Classes:  Course, Student, Instructor,  Assignment
# Requirements:
# Enroll students, assign instructors
# Use submit() method differently for types of assignments

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []
        self.instructor = None
        self.assignments = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.title}")

    def assign_instructor(self, instructor):
        self.instructor = instructor
        print(f"{instructor.name} assigned as instructor for {self.title}")

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' added to {self.title}")

    def __str__(self):
        return (f"Course: {self.title} (ID: {self.course_id})\n"
                f"Instructor: {self.instructor.name if self.instructor else 'None'}\n"
                f"Students: {', '.join(s.name for s in self.students)}\n"
                f"Assignments: {', '.join(a.title for a in self.assignments)}")

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

class Student(Person):
    def submit(self, assignment):
        assignment.submit(self)

class Instructor(Person):
    pass

class Assignment:
    def __init__(self, assignment_id, title):
        self.assignment_id = assignment_id
        self.title = title

    def submit(self, student):
        raise NotImplementedError("Subclass must implement submit method")

class QuizAssignment(Assignment):
    def submit(self, student):
        print(f"{student.name} submitted Quiz '{self.title}' online.")

class ProjectAssignment(Assignment):
    def submit(self, student):
        print(f"{student.name} submitted Project '{self.title}' with a report.")

def main():
    # Create course
    course = Course(1, "Python Programming")

    # Create instructor and students
    instructor = Instructor(100, "Dr. Smith")
    student1 = Student(201, "Nisha")
    student2 = Student(202, "Ravi")

    # Assign instructor and enroll students
    course.assign_instructor(instructor)
    course.enroll_student(student1)
    course.enroll_student(student2)

    # Create assignments
    quiz = QuizAssignment(301, "Chapter 1 Quiz")
    project = ProjectAssignment(302, "Final Project")

    course.add_assignment(quiz)
    course.add_assignment(project)

    # Students submit assignments (polymorphism in submit)
    student1.submit(quiz)
    student2.submit(project)

    # Print course info
    print()
    print(course)

if __name__ == "__main__":
    main()
