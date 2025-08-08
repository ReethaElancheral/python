from flask import Flask

app = Flask(__name__)

# Route: /hello/<name>
@app.route('/hello/<string:name>')
def hello(name):
    return f"""
    <html>
    <head><title>Greeting</title></head>
    <body>
        <h2>Hello, {name.title()}!</h2>
    </body>
    </html>
    """

# Route: /greet/<name>/<time>
@app.route('/greet/<string:name>/<string:time>')
def greet(name, time):
    time = time.lower()

    if 'morning' in time:
        greeting = "Good Morning"
    elif 'afternoon' in time:
        greeting = "Good Afternoon"
    elif 'evening' in time:
        greeting = "Good Evening"
    elif 'night' in time:
        greeting = "Good Night"
    else:
        greeting = "Hello"

    return f"""
    <html>
    <head><title>Personal Greeting</title></head>
    <body>
        <h2>{greeting}, {name.title()}!</h2>
        <p><a href="/hello/{name}">Back to Hello</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
