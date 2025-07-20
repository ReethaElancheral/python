def add_book(books, borrowers, title, borrower, due_date):
    if title in books:
        print(f"The book '{title}' is already lent out.")
        return
    books[title] = (borrower, due_date)
    borrowers.add(borrower)
    print(f"Book '{title}' lent to {borrower}, due on {due_date}.")

def return_book(books, borrowers, title):
    if title not in books:
        print(f"No record found for book '{title}'.")
        return
    borrower, _ = books.pop(title)
    print(f"Book '{title}' returned by {borrower}.")

def list_books(books):
    if not books:
        print("No books currently lent out.")
        return
    print("\nLent Out Books:")
    for title, (borrower, due_date) in books.items():
        print(f"- {title} → {borrower} (Due: {due_date})")
