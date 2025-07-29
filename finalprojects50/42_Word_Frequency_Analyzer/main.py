import os
from collections import Counter
import string

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def clean_text(text):
    # Remove punctuation and convert to lower case
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def word_frequency(text):
    words = text.split()
    return Counter(words)

def most_common_words(freq_dict, n=10):
    return freq_dict.most_common(n)

def main():
    print("Word Frequency Analyzer")
    filepath = input("Enter path to text file: ").strip()
    if not os.path.isfile(filepath):
        print("File does not exist.")
        return

    try:
        text = read_file(filepath)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    cleaned = clean_text(text)
    freq = word_frequency(cleaned)

    print("\nTop 10 most common words:")
    for word, count in most_common_words(freq):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
