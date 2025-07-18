genres = {"Fiction", "Science", "History", "Technology"}

def add_book(library, isbn, title, author, genre):
    if isbn in library:
        print("Book already exists.")
        return
    if genre not in genres:
        print(f"Genre '{genre}' is not available.")
        return
    library[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "available": True
    }
    print(f"Book '{title}' added.")

def display_books(library):
    if not library:
        print("No books available.")
        return
    for isbn, details in library.items():
        status = "Available" if details["available"] else "Checked out"
        print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Genre: {details['genre']}, Status: {status}")
