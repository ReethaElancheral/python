from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory mood log storage
mood_logs = []

@app.route('/')
def home():
    return '''
        <h2>Welcome to the Daily Mood Logger</h2>
        <ul>
            <li><a href="/log-mood">Log Your Mood</a></li>
            <li><a href="/logs?mood=happy">View Happy Logs</a></li>
        </ul>
        <hr>
    '''

@app.route('/log-mood', methods=['GET', 'POST'])
def log_mood():
    if request.method == 'POST':
        name = request.form['name']
        mood = request.form['mood']
        reason = request.form['reason']

        # Store mood data
        mood_logs.append({
            'name': name,
            'mood': mood.lower(),
            'reason': reason
        })

        return redirect(url_for('thank_you', name=name))

    return '''
        <h2>Log Your Mood</h2>
        <form method="POST">
            Name: <input type="text" name="name" required><br><br>
            Mood: <input type="text" name="mood" required><br><br>
            Reason: <br>
            <textarea name="reason" rows="4" cols="30" required></textarea><br><br>
            <input type="submit" value="Submit Mood">
        </form>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form['name']
    mood = request.form['mood']
    reason = request.form['reason']

    # Store mood data
    mood_logs.append({
        'name': name,
        'mood': mood.lower(),
        'reason': reason
    })

    return f'''
        <h2>Mood Submitted</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Mood:</strong> {mood}</p>
        <p><strong>Reason:</strong> {reason}</p>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/logs')
def view_logs():
    mood_filter = request.args.get('mood', '').lower()
    filtered = [entry for entry in mood_logs if entry['mood'] == mood_filter]

    if not filtered:
        return f'''
            <h2>No logs found for mood: {mood_filter}</h2>
            <a href="/">Back to Home</a>
            <hr>
        '''

    items = ''.join([f"<li>{entry['name']} felt {entry['mood']} because {entry['reason']}</li>" for entry in filtered])
    return f'''
        <h2>Logs for Mood: {mood_filter.title()}</h2>
        <ul>{items}</ul>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/thank-you/<name>')
def thank_you(name):
    return f'''
        <h2>Thank You, {name.title()}!</h2>
        <p>Your mood has been successfully logged.</p>
        <a href="/">Back to Home</a>
        <hr>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
