#  Task 30: Demonstrate Absolute and Relative Imports

from shopping_cart.cart import create_cart, add_item, remove_item, total
from shopping_cart.checkout import process_checkout

cart = create_cart()
add_item(cart, "Laptop", 999.99)
add_item(cart, "Mouse", 25.50)
cart = remove_item(cart, "Mouse")
process_checkout(cart)

