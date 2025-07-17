

def capitalize_text(text):
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def word_count(text):
    """Return the number of words in the text."""
    return len(text.split())

def find_keywords(text, keywords):
    """Return a list of keywords found in the text."""
    return [word for word in keywords if word in text]
