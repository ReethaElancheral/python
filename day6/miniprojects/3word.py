# 🧩 3. Word Analyzer Tool

# Topics Covered: *args, string operations, lambda, map()
# Requirements:
# Accept multiple words
# Print word lengths using map()
# Use lambda to convert words to uppercase
# Return most frequent character in each word

def word_analyzer(*words):
    print("\n📏 Word Lengths:")
    lengths = list(map(len, words))
    for word, length in zip(words, lengths):
        print(f"{word} → {length} characters")

    print("\n🔠 Words in Uppercase:")
    upper_words = list(map(lambda w: w.upper(), words))
    for word in upper_words:
        print(word)

    print("\n🔁 Most Frequent Character in Each Word:")
    for word in words:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        most_freq = max(freq.items(), key=lambda item: item[1])[0]
        print(f"{word} → '{most_freq}'")

        
word_analyzer("banana", "apple", "success", "google")
