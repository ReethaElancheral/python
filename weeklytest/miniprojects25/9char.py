# 9. Character Frequency Counter

# Concepts: strings, lists, functions.
# Input a sentence.
# Count frequency of each character.
# Return output in dictionary or formatted string.
# Use functions to handle logic.


def count_char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def print_frequency(freq):
    print("\n=== Character Frequency ===")
    for char, count in sorted(freq.items()):
     
        display_char = char if char != ' ' else '[space]'
        print(f"'{display_char}': {count}")

sentence = input("Enter a sentence: ")
frequency = count_char_frequency(sentence)
print_frequency(frequency)
