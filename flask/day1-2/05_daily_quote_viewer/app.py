from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Hardcoded weekly quotes
quotes = {
    'monday': "Start your week strong!",
    'tuesday': "Keep pushing forward.",
    'wednesday': "Halfway to the weekend!",
    'thursday': "Stay focused and consistent.",
    'friday': "Finish strong!",
    'saturday': "Relax and recharge.",
    'sunday': "Plan and prepare for success."
}

# Home Route: Shows today's quote
@app.route('/')
def home():
    today = datetime.now().strftime('%A').lower()
    quote = quotes.get(today, "No quote available today.")
    return f"""
    <html>
    <head><title>Daily Quote</title></head>
    <body style="background:#f0f8ff; padding:30px; font-family:sans-serif;">
        <h1 style="color:#333;">Quote for Today ({today.title()}):</h1>
        <p style="font-size:24px; color:#0066cc;">"{quote}"</p>
        <hr>
        <p>Try another day manually: <a href="/quote/monday">/quote/monday</a></p>
    </body>
    </html>
    """

# Dynamic Route: /quote/<day>
@app.route('/quote/<string:day>')
def quote_by_day(day):
    quote = quotes.get(day.lower(), "No quote found for that day.")
    return f"""
    <html>
    <head><title>Quote for {day.title()}</title></head>
    <body style="background:#fff8dc; padding:30px; font-family:sans-serif;">
        <h1 style="color:#444;">Quote for {day.title()}:</h1>
        <p style="font-size:22px; color:#b22222;">"{quote}"</p>
        <p><a href="/">Back to today</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
