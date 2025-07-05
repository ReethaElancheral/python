# ✅ 14. Alphabet Counter

# Objective: Count vowels, consonants, digits, and special characters.
# Requirements:
# Input: string.
# Use for loop + if conditions + in + .isalpha() or .isdigit().
# Maintain counters.
# Display result.

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_chars = 0

vowel_letters = "aeiouAEIOU"

for char in text:
    if char.isalpha():
        if char in vowel_letters:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char != " ": 
        special_chars += 1

print("\nCharacter Counts:")
print(f"Vowels         : {vowels}")
print(f"Consonants     : {consonants}")
print(f"Digits         : {digits}")
print(f"Special Chars  : {special_chars}")
