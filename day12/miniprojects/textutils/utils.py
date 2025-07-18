# textutils/utils.py
import re
from .config import PUNCTUATION_TABLE

def remove_punctuation(text: str) -> str:
    return text.translate(PUNCTUATION_TABLE)

def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()
