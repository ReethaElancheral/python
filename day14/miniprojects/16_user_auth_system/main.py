from auth.auth_core import signup, login
from auth.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
