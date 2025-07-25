# 10. Cart Item Fetcher 

# Goal: Implement a cart item reader that reads one product at a time from a user's 
# cart. 
# Requirements: 
#  Simulate cart using a list 
#  Create a CartIterator class 
#  Handle empty cart using exception

class CartIterator:
    def __init__(self, cart):
        if not cart:
            raise ValueError("Cart is empty")
        self.cart = cart
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cart):
            raise StopIteration
        item = self.cart[self.index]
        self.index += 1
        return item

# Usage
try:
    cart = ["Apple", "Banana", "Carrot"]
    print("Cart items:")
    for item in CartIterator(cart):
        print(item)

    print("\nTesting empty cart:")
    empty_cart = []
    empty_iter = CartIterator(empty_cart)
except ValueError as e:
    print("Error:", e)
