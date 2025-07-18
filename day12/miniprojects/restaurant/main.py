# restaurant/main.py
import sys
from .orders import create_order
from .bill import calculate_bill, format_bill

def main():
    print("Menu:")
    from .menu import MENU
    for key, (name, price) in MENU.items():
        print(f"  {key}. {name} — ${price:.2f}")

    choices = input("Enter item numbers separated by commas: ")
    try:
        selected = [int(x.strip()) for x in choices.split(',')]
    except ValueError:
        print("Invalid input. Exiting.")
        sys.exit(1)

    order = create_order(selected)
    if not order['items']:
        print("No valid items selected. Exiting.")
        sys.exit(1)

    bill = calculate_bill(order)
    print("\n" + format_bill(order, bill))

if __name__ == "__main__":
    main()
