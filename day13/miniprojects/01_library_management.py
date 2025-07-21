
# 1. Library Management System

# Concepts: Class, Inheritance, Polymorphism, Encapsulation, Abstraction
# Classes:  Book, Member, Librarian,  Library, Transaction
# Requirements:
# Add/remove/search books (title, author, ISBN)
# Borrow/return logic with due date
# Track member activities
# Use private variables for sensitive data
# Use __str__ and __len__ methods


from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True  # Encapsulated availability

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

    def __len__(self):
        return len(self.title)

    @property
    def available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = {}  # book_isbn -> due_date

    def borrow_book(self, book, days=14):
        if book.borrow():
            due_date = datetime.now() + timedelta(days=days)
            self.__borrowed_books[book.isbn] = due_date
            return True, due_date
        return False, None

    def return_book(self, book):
        if book.isbn in self.__borrowed_books:
            book.return_book()
            del self.__borrowed_books[book.isbn]
            return True
        return False

    def borrowed_books(self):
        return self.__borrowed_books.copy()

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Librarian:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Librarian: {self.name}"


class Library:
    def __init__(self):
        self.books = {}  # isbn -> Book

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            return True
        return False

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books.values():
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            results.append(book)
        return results

    def total_books(self):
        return len(self.books)


class Transaction:
    def __init__(self, member, book, transaction_type):
        self.member = member
        self.book = book
        self.transaction_type = transaction_type  # 'borrow' or 'return'
        self.date = datetime.now()

    def __str__(self):
        return (f"{self.transaction_type.title()} - {self.book.title} by "
                f"{self.member.name} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    lib = Library()
    librarian = Librarian("Anita")
    member = Member("Ravi", 1)

    # Add books
    b1 = Book("Python Basics", "Guido van Rossum", "ISBN001")
    b2 = Book("OOP with Python", "Rossum", "ISBN002")
    lib.add_book(b1)
    lib.add_book(b2)

    print(f"Total books in library: {lib.total_books()}")

    # Search books
    results = lib.search_books(title="Python")
    print("Search results:")
    for book in results:
        print(book)

    # Borrow book
    success, due_date = member.borrow_book(b1)
    if success:
        print(f"{member.name} borrowed '{b1.title}', due on {due_date.date()}")
        t1 = Transaction(member, b1, "borrow")
        print(t1)
    else:
        print("Book not available for borrowing.")

    # Return book
    returned = member.return_book(b1)
    if returned:
        t2 = Transaction(member, b1, "return")
        print(t2)
    else:
        print("Return failed, book was not borrowed.")


if __name__ == "__main__":
    main()
