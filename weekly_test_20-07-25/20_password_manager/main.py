from manager.operations import (
    add_account, update_account, delete_account, search_account, list_accounts
)

def main():
    accounts = {}

    while True:
        print("\n--- Password Manager ---")
        print("1. Add Account")
        print("2. Update Account")
        print("3. Delete Account")
        print("4. Search Account")
        print("5. List All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_account(accounts)
        elif choice == '2':
            update_account(accounts)
        elif choice == '3':
            delete_account(accounts)
        elif choice == '4':
            search_account(accounts)
        elif choice == '5':
            list_accounts(accounts)
        elif choice == '6':
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
