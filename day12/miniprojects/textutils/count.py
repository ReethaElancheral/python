# textutils/count.py
from .sanitize import sanitize
from collections import Counter

def word_count(text: str) -> dict:
    clean = sanitize(text)
    if not clean:
        return {}
    words = clean.split()
    return dict(Counter(words))

def char_count(text: str) -> dict:
    clean = sanitize(text).replace(' ', '')
    return dict(Counter(clean))
