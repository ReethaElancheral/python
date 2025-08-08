from flask import Flask, request, redirect, url_for

app = Flask(__name__)
votes = {}
voter_log = {}

@app.route('/poll')
def poll():
    return '''
    <h2>Vote for your choice</h2>
    <form method="POST" action="/vote">
        Name: <input type="text" name="name"><br><br>
        <input type="radio" name="option" value="A"> Option A<br>
        <input type="radio" name="option" value="B"> Option B<br>
        <input type="radio" name="option" value="C"> Option C<br><br>
        <input type="submit" value="Vote">
    </form>
    '''

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['name']
    option = request.form['option']
    votes[option] = votes.get(option, 0) + 1
    voter_log[name.lower()] = option
    return redirect('/result')

@app.route('/result')
def result():
    option = request.args.get('option')
    if option:
        count = votes.get(option.upper(), 0)
        return f"<h3>Votes for Option {option.upper()}: {count}</h3>"
    result_html = "<h2>Poll Results</h2>"
    for k, v in votes.items():
        result_html += f"<p>Option {k}: {v} votes</p>"
    return result_html

@app.route('/voter/<name>')
def voter_choice(name):
    choice = voter_log.get(name.lower())
    return f"<h3>{name} voted for: {choice}</h3>" if choice else "<p>No vote found</p>"

if __name__ == '__main__':
    app.run(debug=True)
