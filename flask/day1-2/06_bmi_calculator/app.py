from flask import Flask

app = Flask(__name__)

# Home route: Usage info
@app.route('/')
def home():
    return """
    <h2>BMI Calculator</h2>
    <p>To use this tool, go to: <code>/bmi/&lt;weight_kg&gt;/&lt;height_m&gt;</code></p>
    <p>Example: <a href="/bmi/70/1.75">/bmi/70/1.75</a></p>
    """

# BMI calculation route
@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    bmi_value = round(bmi_value, 2)

    # Determine BMI Category
    if bmi_value < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi_value < 25:
        category = "Normal weight"
    elif 25 <= bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return f"""
    <h2>Your BMI Result</h2>
    <p><b>Weight:</b> {weight} kg</p>
    <p><b>Height:</b> {height} m</p>
    <p><b>BMI:</b> {bmi_value}</p>
    <p><b>Category:</b> {category}</p>
    <p><a href="/">Back to Home</a></p>
    """

if __name__ == '__main__':
    app.run(debug=True)
