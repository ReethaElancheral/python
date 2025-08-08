from flask import Flask, request, redirect, url_for

app = Flask(__name__)
rsvps = []

@app.route('/rsvp', methods=['GET'])
def rsvp_form():
    return '''
    <h2>RSVP Form</h2>
    <form method="POST" action="/rsvp-confirm">
        Name: <input type="text" name="name"><br><br>
        Email: <input type="email" name="email"><br><br>
        Attending (yes/no): <input type="text" name="attending"><br><br>
        <input type="submit" value="RSVP">
    </form>
    '''

@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form['name']
    email = request.form['email']
    attending = request.form['attending']
    rsvps.append({'name': name, 'email': email, 'attending': attending})
    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {name}, for your RSVP!</h3>"

@app.route('/guests')
def guest_list():
    attending = request.args.get('attending')
    guests = [r for r in rsvps if r['attending'].lower() == attending.lower()] if attending else rsvps
    html = "<h2>Guest List</h2>"
    for g in guests:
        html += f"<p>{g['name']} - {g['attending']}</p>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
