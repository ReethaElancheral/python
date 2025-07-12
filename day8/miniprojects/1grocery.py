# 1. Grocery Cart System

# Description: Build a program to manage a user’s shopping cart.
# Add items using append() and extend().
# Display items using for loop.
# Remove items using remove() or pop().
# Show total count using len() and check for duplicates.
# Use slicing to show first 3 items in the cart.


cart = []

def show_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\n🛒 Items in your cart:")
        for index, item in enumerate(cart, 1):
            print(f"{index}. {item}")
        print(f"Total items: {len(cart)}")

def add_item():
    item = input("Enter an item to add: ")
    cart.append(item)
    print(f"'{item}' added to cart.")

def add_multiple_items():
    items = input("Enter multiple items separated by commas: ").split(",")
    cleaned_items = [item.strip() for item in items]
    cart.extend(cleaned_items)
    print(f"Items added: {cleaned_items}")

def remove_item():
    item = input("Enter an item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from cart.")
    else:
        print(f"'{item}' is not in the cart.")

def pop_last_item():
    if cart:
        removed = cart.pop()
        print(f"Removed last item: {removed}")
    else:
        print("Cart is empty.")

def check_duplicates():
    duplicates = set([item for item in cart if cart.count(item) > 1])
    if duplicates:
        print("Duplicate items found:", list(duplicates))
    else:
        print("No duplicates found.")

def show_first_three():
    print("First 3 items in cart:", cart[:3])


while True:
    print("\n--- Grocery Cart Menu ---")
    print("1. Add item")
    print("2. Add multiple items")
    print("3. Remove item")
    print("4. Pop last item")
    print("5. Show cart")
    print("6. Check for duplicates")
    print("7. Show first 3 items")
    print("8. Exit")

    choice = input("Enter your choice (1–8): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        add_multiple_items()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        pop_last_item()
    elif choice == "5":
        show_cart()
    elif choice == "6":
        check_duplicates()
    elif choice == "7":
        show_first_three()
    elif choice == "8":
        print("Goodbye! 🛒")
        break
    else:
        print("Invalid choice. Please enter 1–8.")
