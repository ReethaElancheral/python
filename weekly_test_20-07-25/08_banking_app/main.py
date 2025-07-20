from auth import authenticate, users_db
from bank_ops import deposit, withdraw, view_statement, get_unique_transaction_types

def main():
    print("=== Welcome to Simple Bank ===")
    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password)
    if not user:
        print("Invalid credentials.")
        return

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. View Statement")
        print("4. Unique Transaction Types")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: ₹"))
            deposit(user, amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: ₹"))
            withdraw(user, amt)
        elif choice == "3":
            view_statement(user)
        elif choice == "4":
            types = get_unique_transaction_types(user)
            print("Unique Transactions:", types)
        elif choice == "5":
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
