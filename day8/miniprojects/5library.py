# 5. Library Book Catalog

# Description: Track books in a library.
# Create a list of books (title, author).
# Add/remove/update book details.
# Search for a book using in and index().
# Slice list for "recent additions".

catalog = [
    ["The Alchemist", "Paulo Coelho"],
    ["1984", "George Orwell"],
    ["The Great Gatsby", "F. Scott Fitzgerald"]
]

def show_catalog():
    if not catalog:
        print("📚 Library catalog is empty.")
    else:
        print("\n📖 Library Book Catalog:")
        for i, book in enumerate(catalog, 1):
            print(f"{i}. '{book[0]}' by {book[1]}")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    catalog.append([title, author])
    print(f"'{title}' by {author} added to catalog.")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in catalog:
        if book[0].lower() == title.lower():
            catalog.remove(book)
            print(f"'{title}' removed from catalog.")
            return
    print(f"'{title}' not found.")

def update_book():
    title = input("Enter the title of the book to update: ").strip()
    for i, book in enumerate(catalog):
        if book[0].lower() == title.lower():
            new_title = input("Enter new title (press Enter to keep unchanged): ").strip()
            new_author = input("Enter new author (press Enter to keep unchanged): ").strip()

            if new_title:
                catalog[i][0] = new_title
            if new_author:
                catalog[i][1] = new_author

            print("Book details updated.")
            return
    print(f"'{title}' not found in catalog.")

def search_book():
    title = input("Enter book title to search: ").strip()
    titles = [book[0].lower() for book in catalog]
    if title.lower() in titles:
        index = titles.index(title.lower())
        print(f"✅ Found: '{catalog[index][0]}' by {catalog[index][1]}")
    else:
        print(f"❌ '{title}' not found in catalog.")

def recent_additions():
    print("\n📌 Recently Added Books (last 3):")
    if len(catalog) <= 3:
        for book in catalog:
            print(f"'{book[0]}' by {book[1]}")
    else:
        for book in catalog[-3:]:  
            print(f"'{book[0]}' by {book[1]}")


while True:
    print("\n--- Library Catalog Menu ---")
    print("1. Show All Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Update Book")
    print("5. Search for Book")
    print("6. Show Recent Additions")
    print("7. Exit")

    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        show_catalog()
    elif choice == "2":
        add_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        recent_additions()
    elif choice == "7":
        print("Exiting Library Catalog. Goodbye! 📚")
        break
    else:
        print("Invalid option. Choose between 1–7.")
