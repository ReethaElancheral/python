from cart.operations import add_to_cart, remove_from_cart, checkout

products = {
    "P001": ("Laptop", 50000, 10),
    "P002": ("Headphones", 2000, 25),
    "P003": ("Mouse", 500, 50),
}

cart = []

if __name__ == "__main__":
    add_to_cart(cart, products, "P001", 1)
    add_to_cart(cart, products, "P002", 2)
    remove_from_cart(cart, "P002", 1)
    checkout(cart, products)
