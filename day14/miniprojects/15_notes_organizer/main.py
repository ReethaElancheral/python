from notes.organizer import add_note, view_notes, search_notes
from notes.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Add Note")
        print("2. View Notes by Category")
        print("3. Search Notes")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            print("Exiting Notes Organizer.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
