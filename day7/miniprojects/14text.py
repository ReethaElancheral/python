# 14. Text Highlighter

# Concepts: .replace(), .upper(), .count()
# Input: paragraph and keyword
# Replace all occurrences of keyword with uppercase keyword
# Count how many times it appeared



paragraph = input("Enter a paragraph:\n")
keyword = input("Enter keyword to highlight: ").strip()

lower_paragraph = paragraph.lower()
lower_keyword = keyword.lower()
count = lower_paragraph.count(lower_keyword)

words = paragraph.split()
highlighted_words = [
    word.upper() if word.lower() == lower_keyword else word
    for word in words
]
highlighted_paragraph = " ".join(highlighted_words)

print("\n--- Highlighted Paragraph ---")
print(highlighted_paragraph)
print(f"\nKeyword '{keyword}' appeared {count} times.")

