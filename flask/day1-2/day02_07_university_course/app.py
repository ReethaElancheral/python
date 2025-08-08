from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Dummy course data
courses = [
    {'code': 'CS101', 'name': 'Intro to Computer Science', 'dept': 'CS'},
    {'code': 'CS102', 'name': 'Data Structures', 'dept': 'CS'},
    {'code': 'EE101', 'name': 'Basic Electronics', 'dept': 'EE'},
    {'code': 'ME101', 'name': 'Thermodynamics', 'dept': 'ME'},
    {'code': 'CS103', 'name': 'Algorithms', 'dept': 'CS'},
    {'code': 'EE102', 'name': 'Circuits', 'dept': 'EE'}
]

@app.route('/')
def home():
    return '''
        <h2>Welcome to the University Portal</h2>
        <ul>
            <li><a href="/courses">View Courses</a></li>
            <li><a href="/register">Register for a Course</a></li>
        </ul>
        <hr>
    '''

@app.route('/courses')
def course_list():
    dept = request.args.get('dept')
    if dept:
        filtered = [c for c in courses if c['dept'].lower() == dept.lower()]
        if not filtered:
            return f"<h3>No courses found for department: {dept}</h3><a href='/courses'>Back</a><hr>"
    else:
        filtered = courses

    course_html = ''.join(f"<li>{c['code']} - {c['name']} ({c['dept']})</li>" for c in filtered)

    return f'''
        <h2>Course List</h2>
        <form method="get">
            <label>Filter by Department:</label>
            <input type="text" name="dept" placeholder="e.g., CS">
            <input type="submit" value="Search">
        </form>
        <ul>{course_html}</ul>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student = request.form['student']
        course = request.form['course']
        print(f"New registration: {student} for {course}")
        return redirect(url_for('confirm_registration', name=student))
    
    return '''
        <h2>Register for a Course</h2>
        <form method="post">
            <label>Student Name:</label><br>
            <input type="text" name="student"><br><br>
            <label>Course Code:</label><br>
            <input type="text" name="course"><br><br>
            <input type="submit" value="Register">
        </form>
        <hr>
    '''

@app.route('/confirm-registration/<name>')
def confirm_registration(name):
    return f'''
        <h2>Thank you, {name}!</h2>
        <p>Your registration is confirmed.</p>
        <a href="/">Back to Home</a>
        <hr>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
