# 🧩 19. Unique Word Counter

# Topics Covered: function, set, string, return
# Requirements:
# Accept a paragraph
# Return total word count and unique word count
# Optionally return longest word

def unique_word_counter(paragraph):
    words = paragraph.split()
    
    total_words = len(words)
    
    unique_words = set(word.lower() for word in words)
    unique_count = len(unique_words)
    
 
    longest_word = max(words, key=len) if words else ""
    
    return total_words, unique_count, longest_word

text = input("Enter a paragraph: ")
total, unique, longest = unique_word_counter(text)
print(f"Total words: {total}")
print(f"Unique words: {unique}")
print(f"Longest word: {longest}")
