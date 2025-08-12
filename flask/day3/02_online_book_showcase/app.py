from flask import Flask, render_template

app = Flask(__name__)

# Sample book list
books = [
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "cover": "book1.jpg"},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "cover": "book2.jpg"},
    {"name": "1984", "author": "George Orwell", "cover": "book3.jpg"}
]

@app.route("/books")
def books_page():
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
