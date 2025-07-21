# 10. College Admission System

# Concepts: Inheritance, Encapsulation, Aggregation, super()
# Classes:  Person, Student, AdmissionForm,  Department
# Requirements:
# Collect data, verify documents
# Allocate department
# Use super() to call parent constructor
# Aggregate department in student

class Person:
    def __init__(self, name, age):
        self._name = name       # protected
        self._age = age         # protected

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}"

class Department:
    def __init__(self, dept_name, dept_code):
        self.dept_name = dept_name
        self.dept_code = dept_code

    def __str__(self):
        return f"{self.dept_name} ({self.dept_code})"

class AdmissionForm:
    def __init__(self, student, documents_submitted):
        self.student = student
        self.documents_submitted = documents_submitted

    def verify_documents(self):
        # simple check: all required docs present
        required_docs = {"ID Proof", "Marksheet", "Photo"}
        if required_docs.issubset(self.documents_submitted):
            print("Documents verified successfully.")
            return True
        else:
            missing = required_docs - set(self.documents_submitted)
            print(f"Missing documents: {', '.join(missing)}")
            return False

class Student(Person):
    def __init__(self, name, age, student_id, department=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.department = department  # aggregation

    def allocate_department(self, department):
        self.department = department
        print(f"Department {department} allocated to {self._name}")

    def __str__(self):
        dept_info = str(self.department) if self.department else "Not allocated"
        return (f"Student ID: {self.student_id}, {self.get_details()}, "
                f"Department: {dept_info}")

def main():
    # Create department
    cs_dept = Department("Computer Science", "CS")

    # Create student
    student = Student("Nisha", 18, "S101")

    # Create admission form and verify docs
    form = AdmissionForm(student, ["ID Proof", "Marksheet", "Photo"])
    if form.verify_documents():
        student.allocate_department(cs_dept)
    else:
        print("Cannot allocate department until documents verified.")

    # Print student info
    print(student)

if __name__ == "__main__":
    main()
