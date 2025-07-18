from inventory.inventory_ops import add_device, display_inventory

def main():
    inventory = {}
    brands_set = set()

    while True:
        print("\n=== Tech Inventory App ===")
        print("1. Add Device")
        print("2. View Inventory")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            device_type = input("Enter device type (e.g., LAP, MOB): ")
            try:
                number = int(input("Enter device number: "))
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                price = float(input("Enter price: "))
            except ValueError:
                print("Invalid input.")
                continue

            add_device(inventory, brands_set, device_type, number, brand, model, price)

        elif choice == '2':
            display_inventory(inventory, brands_set)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
