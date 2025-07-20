def add_book(title, author, year, genres, books):
    info = (title, author, year)
    book = {"info": info, "genres": genres, "available": True}
    books.append(book)
    print(f"Book '{title}' added.")

def search_books(query, books):
    found = False
    for book in books:
        title, author, _ = book["info"]
        if query.lower() in title.lower() or query.lower() in author.lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{title} by {author} ({status})")
            found = True
    if not found:
        print("No books found.")

def list_genres(books):
    all_genres = set()
    for book in books:
        all_genres.update(book["genres"])
    return all_genres
