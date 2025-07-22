from profileapp.operations import (
    add_profile, view_profiles, update_profile, delete_profile
)
from profileapp.display import show_menu

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            add_profile()
        elif choice == "2":
            view_profiles()
        elif choice == "3":
            update_profile()
        elif choice == "4":
            delete_profile()
        elif choice == "5":
            print("Exiting Profile Storage App.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
