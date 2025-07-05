# ✅ 2. Vowel Counter App

# Objective: Count vowels in a user-entered sentence.
# Requirements:
# Input: any string.
# Use a for loop to iterate through each character.
# Use if to check if the character is a vowel using in.
# Use .lower() to handle case-insensitive comparison.
# Display total vowel count.

sentence = input("Enter a sentence: ")

vowels = "aeiou"
count = 0


for char in sentence:
    if char.lower() in vowels:
        count += 1
print(f"Total vowels in the sentence: {count}")
