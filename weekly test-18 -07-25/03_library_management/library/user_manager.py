def checkout_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return
    if not library[isbn]["available"]:
        print("Book already checked out.")
        return
    library[isbn]["available"] = False
    print(f"You have checked out '{library[isbn]['title']}'.")

def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return
    if library[isbn]["available"]:
        print("Book was not checked out.")
        return
    library[isbn]["available"] = True
    print(f"You have returned '{library[isbn]['title']}'.")
