from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Chocolate Cake", "price": 15.99, "in_stock": True, "image": "product1.jpg"},
    {"name": "Blueberry Muffin", "price": 3.99, "in_stock": False, "image": "product2.jpg"},
    {"name": "Croissant", "price": 2.99, "in_stock": True, "image": "product3.jpg"}
]

@app.route("/products")
def products_page():
    return render_template("products.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
