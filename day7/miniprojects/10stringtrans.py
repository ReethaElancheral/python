# 10. String Transformer

# Concepts: .replace(), upper(), lower(), title()
# Input a sentence
# Provide 4 versions:
# All uppercase
# All lowercase
# Title case
# Replace all spaces with underscores

sentence = input("Enter a sentence: ").strip()

uppercase_version = sentence.upper()
lowercase_version = sentence.lower()
titlecase_version = sentence.title()
underscore_version = sentence.replace(" ", "_")

print("\n--- String Transformations ---")
print("Uppercase:         ", uppercase_version)
print("Lowercase:         ", lowercase_version)
print("Title Case:        ", titlecase_version)
print("Underscore Format: ", underscore_version)
