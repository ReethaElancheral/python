# ✅ 7. Vowel Remover Tool

# Objective: Remove vowels from a given sentence.
# Requirements:
# Input: sentence.
# Use for loop with continue to skip vowels.
# Use a new string to collect non-vowel characters.
# Display the filtered sentence.


sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
result = ""

for char in sentence:
    if char in vowels:
        continue 
    result += char 

print("Sentence without vowels:")
print(result)
