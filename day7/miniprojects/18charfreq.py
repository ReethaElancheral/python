# 18. Character Frequency Analyzer

# Concepts: .count(), loop through .lower() string
# Input: sentence
# Print how many times each vowel appears

sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"

print("\n--- Vowel Frequency ---")
for vowel in vowels:
    count = sentence.count(vowel)
    print(f"{vowel}: {count}")
