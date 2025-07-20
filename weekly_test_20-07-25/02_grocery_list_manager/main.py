
from grocery.operations import add_item, remove_item, mark_bought, search_item
from grocery.display import show_items

def main():
    grocery_data = {}  
    bought_items = set()

    while True:
        print("\n1. Add  2. Remove  3. Mark Bought  4. Show  5. Search  6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Item name: ")
            cat = input("Category: ")
            add_item(name, cat, grocery_data)

        elif choice == "2":
            name = input("Item to remove: ")
            remove_item(name, grocery_data)

        elif choice == "3":
            name = input("Item to mark bought: ")
            mark_bought(name, bought_items)

        elif choice == "4":
            show_items(grocery_data, bought_items)

        elif choice == "5":
            keyword = input("Search for: ")
            results = search_item(keyword, grocery_data)
            print("\nFound:")
            for r in results:
                print(f"{r[0]} in {r[1]}")

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
