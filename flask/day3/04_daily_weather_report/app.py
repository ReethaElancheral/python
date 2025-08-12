import json
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/weather")
def weather():
    weather_data = {
        "date": date.today().strftime("%B %d, %Y"),
        "temperature": 32,
        "condition": "Sunny",
        "temps_week": [28, 30, 32, 33, 31, 29, 27]
    }
    temps_json = json.dumps(weather_data["temps_week"])
    return render_template("weather.html", weather=weather_data, temps_json=temps_json)

if __name__ == "__main__":
    app.run(debug=True)
