from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "title": "The Great Adventure",
        "poster": "movie1.jpg",
        "new_release": True,
        "rating": 4
    },
    {
        "title": "Romantic Escape",
        "poster": "movie2.jpg",
        "new_release": False,
        "rating": 3
    },
    {
        "title": "Mystery Night",
        "poster": "movie3.jpg",
        "new_release": True,
        "rating": 5
    }
]

@app.route("/movies")
def movies_page():
    return render_template("movies.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
