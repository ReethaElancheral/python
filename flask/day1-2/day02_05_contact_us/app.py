from flask import Flask, request, redirect, url_for, flash
from flask import render_template_string

app = Flask(__name__)
app.secret_key = 'secret'  # Needed for flashing

contacts = []

@app.route('/contact', methods=['GET'])
def contact_form():
    return '''
    <h2>Contact Us</h2>
    <form method="POST" action="/submit?source=homepage">
        Name: <input type="text" name="name"><br><br>
        Email: <input type="email" name="email"><br><br>
        Message: <textarea name="message"></textarea><br><br>
        Department:
        <select name="department">
            <option value="Sales">Sales</option>
            <option value="Support">Support</option>
            <option value="HR">HR</option>
        </select><br><br>
        <input type="submit" value="Send">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    department = request.form['department']
    source = request.args.get('source')

    contacts.append({'name': name, 'email': email, 'message': message, 'department': department, 'source': source})
    flash(f"Thanks {name}, your message to {department} was received from {source} page!")
    return redirect('/contact/thank-you')

@app.route('/contact/thank-you')
def thank_you_contact():
    # Showing flash messages
    html = "<h3>Thank you for contacting us!</h3>"
    from flask import get_flashed_messages
    for msg in get_flashed_messages():
        html += f"<p>{msg}</p>"
    return html

@app.route('/contact/<department>')
def department_page(department):
    dept_contacts = [c for c in contacts if c['department'].lower() == department.lower()]
    if not dept_contacts:
        return f"<h3>No messages yet for {department}</h3>"
    html = f"<h2>Messages for {department}</h2>"
    for c in dept_contacts:
        html += f"<p><b>{c['name']}</b>: {c['message']}</p>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
