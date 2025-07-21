# 8. Online Exam Portal

# Concepts: Class, Inheritance, Encapsulation, Abstraction
# Classes:  User, Student, Admin, Exam, Question
# Requirements:
# Admin adds exams/questions
# Student appears for exams
# Track scores, show results
# Use private data for answers

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_role(self):
        pass

class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.__answers = {}  # private: exam_id -> {question_id: answer}
        self.scores = {}     # exam_id -> score

    def get_role(self):
        return "Student"

    def answer_question(self, exam, question_id, answer):
        if exam.exam_id not in self.__answers:
            self.__answers[exam.exam_id] = {}
        self.__answers[exam.exam_id][question_id] = answer

    def take_exam(self, exam):
        print(f"\n{self.username} is taking exam: {exam.title}")
        for q in exam.questions:
            ans = input(f"Q{q.question_id}: {q.text} = ")
            self.answer_question(exam, q.question_id, ans)
        self.calculate_score(exam)

    def calculate_score(self, exam):
        correct = 0
        total = len(exam.questions)
        for q in exam.questions:
            student_ans = self.__answers[exam.exam_id].get(q.question_id)
            if student_ans is not None and student_ans.strip().lower() == q.correct_answer.lower():
                correct += 1
        score = (correct / total) * 100 if total else 0
        self.scores[exam.exam_id] = score
        print(f"{self.username}'s Score: {score:.2f}%")

class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def get_role(self):
        return "Admin"

    def add_exam(self, portal, exam):
        portal.exams.append(exam)
        print(f"Exam '{exam.title}' added to portal.")

    def add_question(self, exam, question):
        exam.questions.append(question)
        print(f"Question '{question.text}' added to exam '{exam.title}'.")

class Exam:
    def __init__(self, exam_id, title):
        self.exam_id = exam_id
        self.title = title
        self.questions = []

class Question:
    def __init__(self, question_id, text, correct_answer):
        self.question_id = question_id
        self.text = text
        self.correct_answer = correct_answer

class ExamPortal:
    def __init__(self):
        self.exams = []

    def show_exams(self):
        print("Available Exams:")
        for exam in self.exams:
            print(f"- {exam.title} (ID: {exam.exam_id})")

def main():
    portal = ExamPortal()
    admin = Admin("admin1")
    student = Student("Nisha")

    # Admin adds an exam and questions
    exam1 = Exam(101, "Python Basics")
    admin.add_exam(portal, exam1)

    q1 = Question(1, "What keyword is used to define a function?", "def")
    q2 = Question(2, "What symbol starts a comment in Python?", "#")
    admin.add_question(exam1, q1)
    admin.add_question(exam1, q2)

    # Show exams to student
    portal.show_exams()

    # Student takes the exam
    student.take_exam(exam1)

    # Show student score
    print(f"\nFinal Score for {student.username}: {student.scores.get(exam1.exam_id, 'No score')}%")

if __name__ == "__main__":
    main()
