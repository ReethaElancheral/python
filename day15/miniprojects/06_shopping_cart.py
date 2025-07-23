# 6. Shopping Cart Price 

# Use Case: Let user add products and prices, calculate total. 
# Exception Handling Goals:
# Catch invalid price entries (ValueError)
# Raise custom ProductExistsError for duplicates
# Use finally to display total no matter what

# Custom exception for duplicate products
class ProductExistsError(Exception):
    pass

def shopping_cart():
    cart = {}
    total_price = 0

    try:
        while True:
            product = input("Enter product name (or 'done' to finish): ").strip().lower()
            if product == "done":
                break

            if product in cart:
                raise ProductExistsError(f"Product '{product}' already added!")

            try:
                price = float(input(f"Enter price for '{product}': "))
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                cart[product] = price
            except ValueError as ve:
                print(f"❌ Invalid price: {ve}")
            else:
                print(f"✅ Added {product} - ₹{price:.2f}")

    except ProductExistsError as pe:
        print(f"❌ {pe}")

    finally:
        total_price = sum(cart.values())
        print("\n🛒 Shopping Cart Summary:")
        for item, price in cart.items():
            print(f"  {item.capitalize()}: ₹{price:.2f}")
        print(f"\n💰 Total Price: ₹{total_price:.2f}")
        print("🧾 Thank you for shopping!")


if __name__ == "__main__":
    shopping_cart()
