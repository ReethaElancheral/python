from recommender.operations import recommend_books, search_books
from recommender.display import show_books

books = [
    {"title": "1984", "author": "George Orwell", "genres": {"dystopia", "political"}},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genres": {"romance", "classic"}},
    {"title": "Brave New World", "author": "Aldous Huxley", "genres": {"dystopia", "science"}},
    {"title": "Emma", "author": "Jane Austen", "genres": {"romance", "comedy"}},
]

if __name__ == "__main__":
    search_result = search_books(books, "Jane Austen")
    show_books("Search Results", search_result)

    recommended = recommend_books(books, {"romance"})
    show_books("Recommended Books", recommended)
