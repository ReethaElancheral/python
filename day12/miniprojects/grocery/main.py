# grocery/main.py

from grocery.cart import load_cart, add_item, remove_item
from grocery.checkout import checkout

def main():
    cart = load_cart()
    while True:
        print("\nGrocery Shopping System")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ").lower()
            quantity = int(input("Enter quantity: "))
            print(add_item(cart, item_name, quantity))
        elif choice == '2':
            item_name = input("Enter item name to remove: ").lower()
            print(remove_item(cart, item_name))
        elif choice == '3':
            if cart["items"]:
                print("\nYour Cart:")
                for item, details in cart["items"].items():
                    print(f"{item.capitalize()} - Quantity: {details['quantity']}, Total: ${details['total_price']:.2f}")
                print(f"Total: ${cart['total']:.2f}")
            else:
                print("Your cart is empty.")
        elif choice == '4':
            print(checkout(cart))
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
