def show_books(title, book_list):
    print(f"\n{title}")
    print("-" * len(title))
    for book in book_list:
        title_author = (book["title"], book["author"])
        genres = ", ".join(book["genres"])
        print(f"{title_author} - Genres: {genres}")
