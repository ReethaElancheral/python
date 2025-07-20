from lending_tracker.lending_ops import add_book, return_book, list_books
from lending_tracker.reminder_ops import check_overdue

def main():
    books = {}  # title → (borrower, due_date)
    borrowers = set()

    while True:
        print("\n📚 Book Lending Tracker Menu:")
        print("1. Lend a Book")
        print("2. Return a Book")
        print("3. List All Books")
        print("4. Show Overdue Books")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Book title: ").strip()
            borrower = input("Borrower's name: ").strip()
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            add_book(books, borrowers, title, borrower, due_date)

        elif choice == "2":
            title = input("Book title to return: ").strip()
            return_book(books, borrowers, title)

        elif choice == "3":
            list_books(books)

        elif choice == "4":
            check_overdue(books)

        elif choice == "5":
            print("Exiting Book Lending Tracker.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
