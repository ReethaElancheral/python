from flashsale.sale_ops import add_sale, list_products
from flashsale.report_ops import generate_report

def main():
    products = {
        "P1001": {"name": "Laptop", "price": 50000},
        "P1002": {"name": "Smartphone", "price": 25000},
        "P1003": {"name": "Headphones", "price": 3000},
    }

    sales = []

    while True:
        print("\n==== Flash Sale Menu ====")
        print("1. List Products")
        print("2. Add Sale")
        print("3. Sales Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            list_products(products)

        elif choice == '2':
            product_code = input("Enter product code: ").strip()
            buyer = input("Enter buyer name: ").strip()
            qty = int(input("Enter quantity: "))
            add_sale(products, sales, product_code, buyer, qty)

        elif choice == '3':
            generate_report(sales)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
