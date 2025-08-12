from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        "title": "Frontend Developer",
        "company": "TechCorp",
        "remote": True,
        "logo": "company1.png",
        "location": "Remote"
    },
    {
        "title": "Backend Engineer",
        "company": "DataWorks",
        "remote": False,
        "logo": "company2.png",
        "location": "New York, NY"
    },
    {
        "title": "Product Manager",
        "company": "InnovateX",
        "remote": True,
        "logo": "company3.png",
        "location": "Remote"
    }
]

@app.route("/jobs")
def jobs_page():
    return render_template("jobs.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
