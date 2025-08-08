from flask import Flask, request, redirect, url_for

app = Flask(__name__)
applications = []

@app.route('/apply')
def apply():
    return '''
    <h2>Job Application</h2>
    <form method="POST" action="/submit-application">
        Name: <input type="text" name="name"><br><br>
        Email: <input type="email" name="email"><br><br>
        Position: <input type="text" name="position"><br><br>
        <input type="submit" value="Apply">
    </form>
    '''

@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    applications.append({'name': name, 'email': email, 'position': position})
    return redirect('/application-status')

@app.route('/application-status')
def application_status():
    return '<h3>Application Submitted Successfully!</h3>'

@app.route('/applications')
def view_applications():
    position = request.args.get('position')
    filtered = [a for a in applications if a['position'] == position] if position else applications
    html = "<h2>Applications</h2>"
    for a in filtered:
        html += f"<p>{a['name']} - {a['position']}</p>"
    return html

@app.route('/applicant/<name>')
def applicant(name):
    user = next((a for a in applications if a['name'].lower() == name.lower()), None)
    if user:
        return f"<h3>{user['name']}'s Application</h3><p>Email: {user['email']}<br>Position: {user['position']}</p>"
    return "<p>Applicant not found</p>"

if __name__ == '__main__':
    app.run(debug=True)
