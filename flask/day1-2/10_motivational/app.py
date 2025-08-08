from flask import Flask
import random

app = Flask(__name__)

# List of motivational messages
messages = [
    "Believe in yourself and all that you are!",
    "Every day is a second chance.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Stay positive, work hard, make it happen.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don’t stop until you’re proud."
]

# Route: /message → returns random message
@app.route('/message')
def random_message():
    msg = random.choice(messages)
    return f"""
    <html>
    <head>
        <title>Motivational Message</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
                padding-top: 50px;
            }}
            .message {{
                color: #2e8b57;
                font-size: 28px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="message">{msg}</div>
    </body>
    </html>
    """

# Route: /message/<index> → manually select a message
@app.route('/message/<int:index>')
def message_by_index(index):
    if 0 <= index < len(messages):
        msg = messages[index]
    else:
        msg = "Invalid index. Please select from 0 to 6."
    return f"""
    <html>
    <head>
        <title>Motivational Message</title>
        <style>
            body {{
                font-family: Georgia, serif;
                background-color: #fff0f5;
                text-align: center;
                padding-top: 50px;
            }}
            .message {{
                color: #8b0000;
                font-size: 26px;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="message">{msg}</div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
