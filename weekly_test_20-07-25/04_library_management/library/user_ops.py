def borrow_book(title, books):
    for book in books:
        if book["info"][0].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print(f"You borrowed '{title}'.")
            else:
                print(f"'{title}' is already borrowed.")
            return
    print("Book not found.")

def return_book(title, books):
    for book in books:
        if book["info"][0].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print(f"'{title}' returned.")
            else:
                print(f"'{title}' was not borrowed.")
            return
    print("Book not found.")
