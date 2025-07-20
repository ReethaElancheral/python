from library.book_ops import add_book, search_books, list_genres
from library.user_ops import borrow_book, return_book


books = [
    {
        "info": ("The Alchemist", "Paulo Coelho", 1988),
        "genres": {"Fiction", "Philosophy"},
        "available": True
    },
    {
        "info": ("Atomic Habits", "James Clear", 2018),
        "genres": {"Self-Help"},
        "available": True
    }
]

def main():
    while True:
        print("\n1. Add Book  2. Search  3. Genres  4. Borrow  5. Return  6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            genres = set(input("Genres (comma separated): ").split(","))
            add_book(title, author, year, genres, books)

        elif choice == "2":
            query = input("Search by title or author: ")
            search_books(query, books)

        elif choice == "3":
            print("All Genres:", ", ".join(list_genres(books)))

        elif choice == "4":
            title = input("Book to borrow: ")
            borrow_book(title, books)

        elif choice == "5":
            title = input("Book to return: ")
            return_book(title, books)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
