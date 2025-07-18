# textutils/analyze.py
from .count import word_count

def most_common(text: str, n: int = 5) -> list[tuple[str,int]]:
    counts = word_count(text)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]

def unique_words(text: str) -> set[str]:
    return set(word_count(text).keys())
