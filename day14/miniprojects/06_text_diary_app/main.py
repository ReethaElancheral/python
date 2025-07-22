from diary.operations import write_entry, read_entry, edit_entry
from diary.display import show_menu, show_banner

def main():
    show_banner()
    while True:
        choice = show_menu()
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entry()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            print("👋 Exiting Diary App.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
