from library.book_manager import add_book, display_books, genres
from library.user_manager import checkout_book, return_book

def main():
    library = {}

    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            part1 = input("Enter ISBN part 1: ")
            part2 = input("Enter ISBN part 2: ")
            isbn = (part1, part2)

            title = input("Enter book title: ")
            author = input("Enter author name: ")
            print(f"Available genres: {', '.join(genres)}")
            genre = input("Enter genre: ")

            add_book(library, isbn, title, author, genre)

        elif choice == '2':
            display_books(library)

        elif choice == '3':
            isbn = tuple(input("Enter ISBN (part1 part2): ").split())
            checkout_book(library, isbn)

        elif choice == '4':
            isbn = tuple(input("Enter ISBN (part1 part2): ").split())
            return_book(library, isbn)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
