from flask import Flask

app = Flask(__name__)

# Sample portfolio data
portfolio_db = {
    'nisha': {
        'profession': 'Software Developer',
        'skills': ['Python', 'Flask', 'JavaScript', 'React'],
        'projects': [
            {'name': 'Portfolio Website', 'year': 2024},
            {'name': 'Blog Platform', 'year': 2023},
            {'name': 'API Development', 'year': 2024}
        ]
    },
    'john': {
        'profession': 'Data Scientist',
        'skills': ['Python', 'Pandas', 'Machine Learning'],
        'projects': [
            {'name': 'Sales Prediction', 'year': 2023},
            {'name': 'Customer Segmentation', 'year': 2022}
        ]
    }
}

# /portfolio/<name> - Basic profile info
@app.route('/portfolio/<string:name>')
def portfolio(name):
    person = portfolio_db.get(name.lower())
    if not person:
        return f"<h2>No portfolio found for {name.title()}</h2>", 404

    return f"""
    <html>
    <head><title>{name.title()}'s Portfolio</title></head>
    <body>
        <h1>{name.title()}'s Portfolio</h1>
        <p><b>Profession:</b> {person['profession']}</p>
        <p>Check out <a href="/portfolio/{name}/skills">skills</a> and <a href="/portfolio/{name}/projects">projects</a>.</p>
    </body>
    </html>
    """

# /portfolio/<name>/skills - List of skills
@app.route('/portfolio/<string:name>/skills')
def portfolio_skills(name):
    person = portfolio_db.get(name.lower())
    if not person:
        return f"<h2>No skills found for {name.title()}</h2>", 404

    skills_html = "".join(f"<li>{skill}</li>" for skill in person['skills'])
    return f"""
    <html>
    <head><title>{name.title()}'s Skills</title></head>
    <body>
        <h1>{name.title()}'s Skills</h1>
        <ul>
            {skills_html}
        </ul>
        <p><a href="/portfolio/{name}">Back to Portfolio</a></p>
    </body>
    </html>
    """

# /portfolio/<name>/projects - Table of projects
@app.route('/portfolio/<string:name>/projects')
def portfolio_projects(name):
    person = portfolio_db.get(name.lower())
    if not person:
        return f"<h2>No projects found for {name.title()}</h2>", 404

    projects_html = "".join(
        f"<tr><td>{proj['name']}</td><td>{proj['year']}</td></tr>"
        for proj in person['projects']
    )

    return f"""
    <html>
    <head><title>{name.title()}'s Projects</title></head>
    <body>
        <h1>{name.title()}'s Projects</h1>
        <table border="1" cellpadding="8" cellspacing="0">
            <tr><th>Project Name</th><th>Year</th></tr>
            {projects_html}
        </table>
        <p><a href="/portfolio/{name}">Back to Portfolio</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
