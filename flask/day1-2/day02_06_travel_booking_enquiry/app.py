from flask import Flask, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dummy travel deals
travel_deals = {
    'paris': ['Eiffel Tower Package', 'Romantic Getaway'],
    'london': ['London Eye Pass', 'Harry Potter Studio Tour'],
    'tokyo': ['Cherry Blossom Tour', 'Anime City Experience']
}

@app.route('/')
def home():
    return '''
        <h2>Welcome to Travel Booking Enquiry!</h2>
        <p>Go to <a href="/booking">Booking Form</a> or check <a href="/deals?destination=paris">deals</a></p>
        <hr>
    '''

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        destination = request.form['destination']
        date = request.form['travel_date']
        print(f"Booking received: {name} to {destination} on {date}")
        return redirect(url_for('confirm_booking', name=name))
    
    return '''
        <h2>Travel Booking Form</h2>
        <form method="post">
            <label>Name:</label><br>
            <input type="text" name="name"><br><br>
            <label>Destination:</label><br>
            <input type="text" name="destination"><br><br>
            <label>Travel Date:</label><br>
            <input type="date" name="travel_date"><br><br>
            <input type="submit" value="Submit Booking">
        </form>
        <hr>
    '''

@app.route('/booking/confirm/<name>')
def confirm_booking(name):
    return f'''
        <h2>Thank you, {name}!</h2>
        <p>Your booking request has been received.</p>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/deals')
def deals():
    destination = request.args.get('destination', '').lower()
    if destination in travel_deals:
        deals_list = travel_deals[destination]
        deals_html = ''.join(f"<li>{deal}</li>" for deal in deals_list)
        return f'''
            <h2>Deals for {destination.title()}</h2>
            <ul>{deals_html}</ul>
            <a href="/">Back to Home</a>
            <hr>
        '''
    else:
        return '''
            <h2>No deals found for that destination.</h2>
            <a href="/">Back to Home</a>
            <hr>
        '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
