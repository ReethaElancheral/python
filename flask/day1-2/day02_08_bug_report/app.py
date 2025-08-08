from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory bug storage
bug_reports = []

@app.route('/')
def home():
    return '''
        <h2>Bug Reporting System</h2>
        <ul>
            <li><a href="/report">Report a Bug</a></li>
            <li><a href="/bugs">View All Bugs</a></li>
        </ul>
        <hr>
    '''

@app.route('/report', methods=['GET', 'POST'])
def report_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        bug_id = len(bug_reports) + 1

        bug = {
            'id': bug_id,
            'title': title,
            'description': description,
            'priority': priority
        }
        bug_reports.append(bug)

        return redirect(url_for('report_confirm'))

    return '''
        <h2>Report a Bug</h2>
        <form method="post">
            <label>Title:</label><br>
            <input type="text" name="title"><br><br>
            <label>Description:</label><br>
            <textarea name="description"></textarea><br><br>
            <label>Priority:</label><br>
            <select name="priority">
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select><br><br>
            <input type="submit" value="Submit Bug">
        </form>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/submit-report')
def report_confirm():
    return '''
        <h2>Bug Submitted Successfully!</h2>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/bugs')
def view_bugs():
    priority = request.args.get('priority')
    if priority:
        filtered = [b for b in bug_reports if b['priority'].lower() == priority.lower()]
        heading = f'Bugs with Priority: {priority.capitalize()}'
    else:
        filtered = bug_reports
        heading = 'All Reported Bugs'

    if not filtered:
        return f"<h3>No bugs found for priority: {priority}</h3><a href='/bugs'>Back</a><hr>"

    bug_html = ''.join(f"<li><a href='/bug/{b['id']}'>#{b['id']} - {b['title']} ({b['priority']})</a></li>" for b in filtered)

    return f'''
        <h2>{heading}</h2>
        <ul>{bug_html}</ul>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/bug/<int:id>')
def bug_details(id):
    bug = next((b for b in bug_reports if b['id'] == id), None)
    if bug:
        return f'''
            <h2>Bug #{bug['id']} - {bug['title']}</h2>
            <p><strong>Description:</strong> {bug['description']}</p>
            <p><strong>Priority:</strong> {bug['priority'].capitalize()}</p>
            <a href="/bugs">Back to Bug List</a>
            <hr>
        '''
    else:
        return f"<h3>Bug with ID {id} not found.</h3><a href='/bugs'>Back to Bug List</a><hr>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
