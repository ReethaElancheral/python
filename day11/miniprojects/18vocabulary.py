# 18. Vocabulary Builder from Articles

# Goal: Extract unique words from news articles.
# Requirements:
# - Read words from multiple files.
# - Use set comprehension to build a unique vocabulary set.
# - Print words not in the user’s known word list.
# Concepts Covered: Set comp, difference(), file-to-set.

import re

# Sample known vocabulary (user's known words)
known_words = {"data", "analysis", "python", "machine", "learning"}

# Sample list of article file paths
article_files = ["article1.txt", "article2.txt", "article3.txt"]

# Function to extract unique words from articles
def extract_unique_words(files):
    all_words = set()
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().lower()
            words = re.findall(r'\b\w+\b', text)
            all_words.update(words)
    return all_words

# Extract unique words from articles
unique_words = extract_unique_words(article_files)

# Find new words not in the known vocabulary
new_words = unique_words - known_words

# Display new words
print("New words to learn:", new_words)
