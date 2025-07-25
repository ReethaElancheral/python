# 19. Lazy Contact Searcher 
# Objective: Search contacts starting with a character using generators. 
# Requirements: 
#  Use dictionary of names and numbers. 
#  Yield matching contacts using yield. 
#  Use send() to change search key mid-way. 


def lazy_contact_searcher(contacts):
    key = yield "Ready to search. Send starting character."
    while True:
        matches = {name: num for name, num in contacts.items() if name.startswith(key)}
        yield matches
        key = yield "Send another character to search again or stop."

# Example usage:
contacts = {
    "Nisha": "9876543210",
    "Neha": "9123456789",
    "Arjun": "9345678123",
    "Anita": "9012345678",
    "Rakesh": "9090909090"
}

searcher = lazy_contact_searcher(contacts)
print(next(searcher))  # Starts the generator
print(searcher.send("A"))  # Search names starting with 'A'
print(next(searcher))  # Prompt again
print(searcher.send("N"))  # Search names starting with 'N'
