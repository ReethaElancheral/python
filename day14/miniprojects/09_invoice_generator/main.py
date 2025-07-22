from invoice.operations import create_invoice
from invoice.display import show_banner

def main():
    show_banner()
    while True:
        proceed = input("Generate a new invoice? (y/n): ").strip().lower()
        if proceed == "y":
            create_invoice()
        elif proceed == "n":
            print("Exiting Invoice Generator.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
