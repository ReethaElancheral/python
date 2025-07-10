# 9. Word Reverser

# Concepts: slicing, .split(), .join()
# Input: sentence from user
# Reverse each word, maintain word order
# "Hello World" → "olleH dlroW"

sentence = input("Enter a sentence: ").strip()

words = sentence.split()

reversed_words = [word[::-1] for word in words]

result = " ".join(reversed_words)

print("\nReversed Words Sentence:")
print(result)
