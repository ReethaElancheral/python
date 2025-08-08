from flask import Flask

app = Flask(__name__)

# Route 1: Basic user greeting
@app.route('/user/<string:name>')
def greet_user(name):
    print(f"[INFO] /user/{name} was accessed")  # Console log
    return f"<h1>Welcome, {name.title()}!</h1>"

# Route 2: User location greeting
@app.route('/user/<string:name>/location/<string:city>')
def user_location(name, city):
    print(f"[INFO] /user/{name}/location/{city} was accessed")  # Console log
    return f"<p>Hi <b>{name.title()}</b>, how is <b>{city.title()}</b>?</p>"

if __name__ == '__main__':
    app.run(debug=True)
