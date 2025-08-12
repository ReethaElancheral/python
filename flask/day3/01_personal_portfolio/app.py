from flask import Flask, render_template

app = Flask(__name__)


projects = [
    {"title": "Portfolio Website", "description": "Built using Flask and HTML"},
    {"title": "E-commerce App", "description": "Full-stack store application"}
]

@app.route('/')
def home():
    return render_template('home.html', name="John Doe", available=True)

@app.route('/about')
def about():
    skills = ["Python", "Flask", "JavaScript", "CSS"]
    return render_template('about.html', name="John Doe", skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
