import os
from collections import Counter
import string

def analyze_file(filepath):
    if not os.path.isfile(filepath):
        print("❌ File not found.")
        return

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    word_count = len(words)
    char_count = len(text)

    if words:
        freq_word, freq_count = Counter(words).most_common(1)[0]
    else:
        freq_word, freq_count = None, 0

    print(f"\nAnalysis of '{filepath}':")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {char_count}")
    if freq_word:
        print(f"Most Frequent Word: '{freq_word}' ({freq_count} times)")
    else:
        print("No words found in the file.")
