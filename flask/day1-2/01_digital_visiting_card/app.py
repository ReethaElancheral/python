from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/skills/<name>')
def skills(name):
    skill_db = {
        'nisha': ['Python', 'HTML', 'CSS', 'Flask'],
        'john': ['JavaScript', 'React', 'Node.js'],
        'emma': ['Design', 'Figma', 'Illustrator']
    }
    skills_list = skill_db.get(name.lower(), ['No skills found for this person.'])
    return f"<h2>Skills for {name.title()}:</h2><ul>" + "".join(f"<li>{s}</li>" for s in skills_list) + "</ul>"

if __name__ == '__main__':
    app.run(debug=True)
