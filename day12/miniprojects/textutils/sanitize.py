# textutils/sanitize.py
from .utils import remove_punctuation, normalize_whitespace

def sanitize(text: str) -> str:
    text = text.lower()
    text = remove_punctuation(text)
    text = normalize_whitespace(text)
    return text
