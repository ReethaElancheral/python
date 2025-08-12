from flask import Flask, render_template

app = Flask(__name__)

blogs = [
    {
        "title": "Understanding Flask",
        "author": "Jane Doe",
        "snippet": "An introduction to Flask and building web apps...",
        "featured": True,
        "image": "blog1.jpg"
    },
    {
        "title": "JavaScript Tips",
        "author": "John Smith",
        "snippet": "Some handy tips and tricks for JavaScript developers...",
        "featured": False,
        "image": "blog2.jpg"
    },
    {
        "title": "CSS Grid Guide",
        "author": "Emily Johnson",
        "snippet": "Master CSS Grid with this comprehensive guide...",
        "featured": True,
        "image": "blog3.jpg"
    }
]

@app.route("/blogs")
def blogs_page():
    return render_template("blogs.html", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
