# 9. Restaurant Menu System

# Description: Dynamic menu manager.
# Use a list to store dish names and prices.
# Add new dishes, remove sold out items.
# Use nested lists for name-price pairing.


menu = [
    ["Briyani", 250],
    ["Meals", 150],
    ["Chicken Gravy", 220]
]

def show_menu():
    print("\n🍽️ Current Menu:")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item[0]} - ₹{item[1]}")

def add_dish():
    name = input("Enter dish name: ").strip()
    price = input("Enter price: ").strip()
    if price.isdigit():
        menu.append([name, int(price)])
        print(f"{name} added to the menu.")
    else:
        print("Invalid price. Dish not added.")

def remove_dish():
    name = input("Enter dish name to remove (sold out): ").strip().lower()
    for dish in menu:
        if dish[0].lower() == name:
            menu.remove(dish)
            print(f"{dish[0]} removed from menu.")
            return
    print("Dish not found.")


while True:
    print("\n--- Restaurant Menu ---")
    print("1. Show Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Exit")

    choice = input("Choose option (1–4): ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_dish()
    elif choice == "3":
        remove_dish()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice.")
