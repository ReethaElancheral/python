# 19. Book Reading Progress Tracker

# Description: Track books and reading progress.
# Use nested list for [book name, pages read].
# Update page count.
# Check if a book is finished (pages read = total pages).


books = [
    ["The Hobbit", 100, 310],
    ["1984", 50, 328],
    ["Python 101", 120, 120]
]

def show_books():
    if not books:
        print("No books tracked yet.")
    else:
        print("\n📖 Reading Progress:")
        for i, (name, pages_read, total) in enumerate(books, 1):
            status = "Finished" if pages_read >= total else "In Progress"
            print(f"{i}. {name}: {pages_read}/{total} pages ({status})")

def add_book():
    name = input("Enter book name: ").strip()
    total_pages = input("Enter total pages: ").strip()
    if total_pages.isdigit():
        books.append([name, 0, int(total_pages)])
        print(f"Book '{name}' added with {total_pages} pages.")
    else:
        print("Invalid total pages.")

def update_progress():
    show_books()
    if not books:
        return
    index = input("Enter book number to update pages read: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(books):
            pages = input("Enter pages read so far: ").strip()
            if pages.isdigit():
                pages_read = int(pages)
                total = books[index][2]
                if pages_read <= total:
                    books[index][1] = pages_read
                    print(f"Updated '{books[index][0]}' to {pages_read} pages read.")
                else:
                    print("Pages read cannot exceed total pages.")
            else:
                print("Invalid pages input.")
        else:
            print("Invalid book number.")
    else:
        print("Enter a valid number.")

def check_finished():
    finished_books = [b[0] for b in books if b[1] >= b[2]]
    if finished_books:
        print("\n🎉 Finished Books:")
        for book in finished_books:
            print(book)
    else:
        print("No books finished yet.")


while True:
    print("\n--- Book Reading Progress Tracker ---")
    print("1. Show Books and Progress")
    print("2. Add New Book")
    print("3. Update Pages Read")
    print("4. Show Finished Books")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        update_progress()
    elif choice == "4":
        check_finished()
    elif choice == "5":
        print("Exiting Reading Tracker. Happy reading!")
        break
    else:
        print("Invalid choice.")
