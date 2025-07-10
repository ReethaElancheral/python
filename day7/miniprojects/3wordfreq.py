# 3. Word Frequency Counter


# Concepts: .count(), .lower(), .split(), len()
# Input: a paragraph from the user
# Count occurrences of each word using .count()
# Convert string to lowercase for uniformity
# Print total number of words using len() on .split()


paragraph = input("Enter a paragraph:\n")

paragraph = paragraph.lower()

words = paragraph.split()

total_words = len(words)
print("\nTotal number of words:", total_words)

print("\nWord Frequencies:")
unique_words = set(words)  
for word in unique_words:
    print(f"{word}: {words.count(word)}")
