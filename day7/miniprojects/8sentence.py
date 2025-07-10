# 8. Sentence Analyzer

# Concepts: indexing, find(), count(), .split()
# Input: sentence from the user
# Print:
# First character
# Last character
# First space position using find()
# Total vowels and spaces


sentence = input("Enter a sentence: ").strip()

first_char = sentence[0] if sentence else ""
last_char = sentence[-1] if sentence else ""

first_space_pos = sentence.find(" ")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
space_count = sentence.count(" ")

print("\n--- Sentence Analysis ---")
print(f"First character: {first_char}")
print(f"Last character: {last_char}")
print(f"Position of first space: {first_space_pos if first_space_pos != -1 else 'No space found'}")
print(f"Total vowels: {vowel_count}")
print(f"Total spaces: {space_count}")
