from inventory.stock_ops import add_item, remove_item, update_stock, list_by_category, view_inventory
from inventory.alerts import check_restock_alerts

def main():
    inventory = {}
    categories = set()
    suppliers = set()

    while True:
        print("\n=== Simple Inventory System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Stock")
        print("4. List by Category")
        print("5. View Inventory")
        print("6. Restock Alerts")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_item(inventory, categories, suppliers)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            list_by_category(inventory)
        elif choice == "5":
            view_inventory(inventory, suppliers)
        elif choice == "6":
            check_restock_alerts(inventory)
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
