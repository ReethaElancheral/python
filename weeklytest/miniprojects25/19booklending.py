# 19. Book Lending App

# Concepts: lists, while, functions.
# Books available in a list.
# Borrow books (remove from list).
# Return books (add to list).
# Menu-driven loop.

books_available = ["The Hobbit", "1984", "Pride and Prejudice", "To Kill a Mockingbird"]

def show_books():
    if not books_available:
        print("No books are currently available.")
    else:
        print("\nAvailable Books:")
        for i, book in enumerate(books_available, 1):
            print(f"{i}. {book}")

def borrow_book():
    show_books()
    if not books_available:
        return
    book_name = input("Enter the name of the book you want to borrow: ").strip()
    for book in books_available:
        if book.lower() == book_name.lower():
            books_available.remove(book)
            print(f"You borrowed '{book}'. Enjoy reading!")
            return
    print("Sorry, that book is not available.")

def return_book():
    book_name = input("Enter the name of the book you want to return: ").strip()

    if any(book.lower() == book_name.lower() for book in books_available):
        print("This book is already in the library.")
    else:
        books_available.append(book_name)
        print(f"Thank you for returning '{book_name}'.")

while True:
    print("\n--- Book Lending Menu ---")
    print("1. Show available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        show_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Thank you for using the Book Lending App. Goodbye!")
        break
    else:
        print("Invalid choice, please select from 1 to 4.")
