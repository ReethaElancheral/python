# library/search.py

import re
from .catalog import list_ebooks, get_metadata

def search_ebooks(query):
    """Search for eBooks by title."""
    ebooks = list_ebooks()
    matched_books = []
    for ebook in ebooks:
        metadata = get_metadata(ebook)
        if re.search(query, metadata['title'], re.IGNORECASE):
            matched_books.append(metadata)
    return matched_books
