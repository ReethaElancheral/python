from flask import Flask, render_template

app = Flask(__name__)

menu = {
    "Starters": [
        {"name": "Bruschetta", "price": 6.50, "available": True, "image": "starter1.jpg"},
        {"name": "Garlic Bread", "price": 5.00, "available": False, "image": "starter2.jpg"}
    ],
    "Mains": [
        {"name": "Margherita Pizza", "price": 12.00, "available": True, "image": "main1.jpg"},
        {"name": "Spaghetti Carbonara", "price": 14.00, "available": True, "image": "main2.jpg"}
    ],
    "Desserts": [
        {"name": "Tiramisu", "price": 7.00, "available": False, "image": "dessert1.jpg"},
        {"name": "Gelato", "price": 6.00, "available": True, "image": "dessert2.jpg"}
    ]
}

@app.route("/menu")
def menu_page():
    return render_template("menu.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
