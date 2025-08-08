from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Home Route: Shows "We are open!" or "Closed"
@app.route('/')
def home():
    current_hour = datetime.now().hour
    if 9 <= current_hour < 18:  # Open from 9 AM to 6 PM
        status = "<b>We are open!</b>"
    else:
        status = "<b>Closed</b>"
    
    return f"""
    <html>
    <head><title>Business Hours</title></head>
    <body>
        <h1>Welcome to Our Online Store</h1>
        <p>Status: {status}</p>
        <hr>
        <p>Opening Hours: <b>9:00 AM</b> to <b>6:00 PM</b></p>
        <p>Current Server Time: <b>{datetime.now().strftime('%H:%M:%S')}</b></p>
    </body>
    </html>
    """

# Contact Route: Returns contact details with HTML formatting
@app.route('/contact')
def contact():
    return """
    <html>
    <head><title>Contact Us</title></head>
    <body>
        <h2>Contact Information</h2>
        <p><b>Email:</b> support@example.com</p>
        <p><b>Phone:</b> +91-9876543210</p>
        <hr>
        <p>Feel free to reach out during our business hours!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
