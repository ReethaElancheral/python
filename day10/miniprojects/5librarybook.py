# 5. Library Book Catalog

# Description: Manage books in a library.
# Requirements:
# - Book info: {book_id: {"title": ..., "author": ..., "copies": ...}}
# - Add new book
# - Borrow book: reduce copies
# - Return book: increase copies
# - Delete book if copies = 0
# - Use .get() to avoid missing key errors
# - Use .items() to display list of available books


catalog = {}

def add_book(book_id, title, author, copies):
    if book_id in catalog:
        catalog[book_id]["copies"] += copies
    else:
        catalog[book_id] = {"title": title, "author": author, "copies": copies}

def borrow_book(book_id):
    entry = catalog.get(book_id)
    if entry and entry["copies"] > 0:
        entry["copies"] -= 1
        if entry["copies"] == 0:
            catalog.pop(book_id)
        return True
    return False

def return_book(book_id):
    entry = catalog.get(book_id)
    if entry:
        entry["copies"] += 1
        return True
    return False

def display_books():
    print("\n📖 Available Books:")
    print("-------------------------------")
    for bid, info in catalog.items():
        print(f"ID: {bid} | '{info['title']}' by {info['author']} – Copies: {info['copies']}")
    print("-------------------------------")


add_book(1, "1984", "George Orwell", 3)
add_book(2, "To Kill a Mockingbird", "Harper Lee", 2)
add_book(1, "1984", "George Orwell", 2) 

borrow_book(2)        
borrow_book(2)       
borrow_book(2)      

return_book(1)       

display_books()

 