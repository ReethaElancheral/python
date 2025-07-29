from library.library import Library
from library.decorators import admin_only

def main():
    lib = Library()

    while True:
        print("\n📚 Library Management")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. List Available Books")
        print("7. Delete Book (Admin Only)")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            lib.add_book(title, author)

        elif choice == '2':
            keyword = input("Search keyword: ")
            results = lib.search_books(keyword)
            if results:
                for book in results:
                    print(lib.format_book(book))
            else:
                print("No matching books found.")

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            lib.borrow_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            lib.return_book(title)

        elif choice == '5':
            lib.list_books()

        elif choice == '6':
            print("📗 Available Books:")
            for book in lib.available_books():
                print(f"✅ {book.title} by {book.author}")

        elif choice == '7':
            delete_book(lib)

        elif choice == '8':
            lib.save_books()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

@admin_only
def delete_book(lib):
    title = input("Enter book title to delete: ")
    for book in lib.books:
        if book.title.lower() == title.lower():
            lib.books.remove(book)
            print(f"🗑️ '{title}' removed from the library.")
            return
    print("❌ Book not found.")

if __name__ == "__main__":
    main()
