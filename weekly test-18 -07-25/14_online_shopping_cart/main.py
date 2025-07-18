from cart.cart_utils import add_to_cart, view_cart, get_unique_categories

def main():
    cart = {}

    while True:
        print("\n1. Add Item to Cart")
        print("2. View Cart")
        print("3. View Categories")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            item_id = input("Enter Item ID: ").strip()
            name = input("Enter Item Name: ").strip()
            category = input("Enter Category: ").strip().capitalize()
            try:
                price = float(input("Enter Price (₹): "))
            except ValueError:
                print("Invalid price.")
                continue

            add_to_cart(cart, item_id, name, category, price)

        elif choice == "2":
            view_cart(cart)

        elif choice == "3":
            categories = get_unique_categories(cart)
            print("Available Categories:", ", ".join(categories) if categories else "None")

        elif choice == "4":
            print("Exiting Shopping Cart.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
