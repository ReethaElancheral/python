# 17. Word Counter Tool

# Concepts: string, list, functions.
# Input paragraph from user.
# Count words using split().
# Count specific word frequency.

def count_words(text):
    words = text.split()
    return len(words), words

def count_specific_word(words, target):
    target = target.lower()
    count = 0
    for w in words:
        if w.lower() == target:
            count += 1
    return count

paragraph = input("Enter a paragraph:\n")
total_words, word_list = count_words(paragraph)

print(f"\nTotal words: {total_words}")

specific = input("Enter the word to count frequency of: ").strip()
frequency = count_specific_word(word_list, specific)

print(f"The word '{specific}' appears {frequency} time(s).")
