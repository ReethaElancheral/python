from flask import Flask, render_template

app = Flask(__name__)

team = [
    {"name": "Alice Smith", "role": "Team Lead", "photo": "member1.jpg"},
    {"name": "Bob Johnson", "role": "Developer", "photo": "member2.jpg"},
    {"name": "Clara Davis", "role": "Designer", "photo": "member3.jpg"}
]

@app.route("/team")
def team_page():
    return render_template("team.html", team=team)

if __name__ == "__main__":
    app.run(debug=True)
