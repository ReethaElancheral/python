import json
from .book import Book

class Library:
    def __init__(self, data_file='library_data.json'):
        self.books = []
        self.data_file = data_file
        self.load_books()

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"✅ '{title}' added to the library.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower()]
        return results

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"📚 You borrowed '{book.title}'.")
                return
        print("❌ Book not available or already checked out.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"🔄 You returned '{book.title}'.")
                return
        print("❌ Book not found or wasn't borrowed.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        for book in self.books:
            print(book)

    def available_books(self):
        for book in self.books:
            if book.available:
                yield book

    def save_books(self):
        try:
            data = [{"title": b.title, "author": b.author, "available": b.available} for b in self.books]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print("⚠️ Error saving data:", e)

    def load_books(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for entry in data:
                    self.books.append(Book(**entry))
        except FileNotFoundError:
            self.books = []
        except Exception as e:
            print("⚠️ Error loading data:", e)

    @staticmethod
    def format_book(book):
        return f"{book.title.upper()} - {book.author.title()}"
