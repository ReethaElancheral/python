# 3. E-commerce Cart System

# Concepts: Class, Object, Composition, Inheritance, Dunder Methods
# Classes:  Product, Cart, User, Order
# Requirements:
# Add/remove items to cart
# Calculate total cost, apply discounts
# Use __add__, __getitem__, and __contains__
# Use static method for tax calculation

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price  

    def __str__(self):
        return f"{self.name} (₹{self.price})"

    def __eq__(self, other):
        return self.product_id == other.product_id

class Cart:
    def __init__(self):
        self.items = []  

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_item(self, product):
        for i, item in enumerate(self.items):
            if item == product:
                del self.items[i]
                print(f"Removed {product.name} from cart.")
                return True
        print(f"{product.name} not found in cart.")
        return False

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        discount_amount = total * discount_percent / 100
        return total - discount_amount

    # Dunder methods
    def __add__(self, other):
        # Combine two carts
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, product):
        return product in self.items

    def __str__(self):
        if not self.items:
            return "Cart is empty."
        return "Cart items:\n" + "\n".join(f"- {item}" for item in self.items)

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"

class Order:
    TAX_RATE = 5 

    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

    @staticmethod
    def calculate_tax(amount):
        return amount * Order.TAX_RATE / 100

    def calculate_total_with_tax(self):
        total = self.cart.calculate_total()
        tax = self.calculate_tax(total)
        return total + tax

    def __str__(self):
        total = self.cart.calculate_total()
        tax = self.calculate_tax(total)
        grand_total = total + tax
        return (f"Order Summary for {self.user.name}:\n"
                f"Subtotal: ₹{total:.2f}\n"
                f"Tax (@{Order.TAX_RATE}%): ₹{tax:.2f}\n"
                f"Total: ₹{grand_total:.2f}")

def main():
    
    p1 = Product(1, "Smartphone", 15000)
    p2 = Product(2, "Headphones", 2000)
    p3 = Product(3, "Charger", 500)

    # Create user and add items to cart
    user = User(101, "Nisha")
    user.cart.add_item(p1)
    user.cart.add_item(p2)

    print(user.cart)

    # Remove an item
    user.cart.remove_item(p3)  
    user.cart.remove_item(p2) 

    print(user.cart)

    # Check if item in cart
    print(p1 in user.cart)  
    print(p3 in user.cart)  

    # Use dunder add to combine carts
    cart2 = Cart()
    cart2.add_item(p3)
    combined_cart = user.cart + cart2

    print("Combined cart:")
    print(combined_cart)

    # Calculate total and apply discount
    total_before_discount = combined_cart.calculate_total()
    discounted_total = combined_cart.apply_discount(10)  

    print(f"Total before discount: ₹{total_before_discount}")
    print(f"Total after 10% discount: ₹{discounted_total}")

    # Create order and calculate total with tax
    order = Order(user, combined_cart)
    print(order)

if __name__ == "__main__":
    main()
