import argparse
import json
import os
from school.students.register import register_student
from school.students.report import student_report
from school.teachers.register import register_teacher
from school.teachers.report import teacher_report
from school.subjects.register import register_subject
from school.subjects.report import subject_report





DATA_FILE = 'school_data.json'

def save_data():
    data = {
        'students': student_report(),
        'teachers': teacher_report(),
        'subjects': subject_report()
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add-student', nargs=2, metavar=('id', 'name'))
    parser.add_argument('--add-teacher', nargs=2, metavar=('id', 'name'))
    parser.add_argument('--add-subject', nargs=2, metavar=('id', 'title'))
    parser.add_argument('--report', choices=['students','teachers','subjects'])
    args = parser.parse_args()

    if args.add_student:
        sid, name = args.add_student
        register_student(sid, name)
        save_data()
        print("Student added.")
    elif args.report:
        data = load_data()
        print(json.dumps(data.get(args.report, []), indent=2))
