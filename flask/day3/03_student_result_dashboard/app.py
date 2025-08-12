from flask import Flask, render_template

app = Flask(__name__)

@app.route("/result")
def result():
    student_name = "Alice Johnson"
    subjects = [
        {"name": "Math", "marks": 92},
        {"name": "Science", "marks": 85},
        {"name": "English", "marks": 78},
        {"name": "History", "marks": 88}
    ]

    # Calculate average
    avg_marks = sum(subject["marks"] for subject in subjects) / len(subjects)

    # Determine grade
    if avg_marks >= 85:
        grade = "A"
    elif avg_marks >= 70:
        grade = "B"
    else:
        grade = "C"

    return render_template("result.html", student=student_name, subjects=subjects, grade=grade)

if __name__ == "__main__":
    app.run(debug=True)
