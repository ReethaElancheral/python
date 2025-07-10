# 11. Feedback Cleaner Tool

# Concepts: .strip(), .replace(), .count(), len()
# Input feedback like "  I love it!!!  "
# Clean extra spaces, remove !, count words and characters

feedback = input("Enter your feedback: ")

cleaned = feedback.strip()           
cleaned = cleaned.replace("!", "")   

char_count = len(cleaned)
word_count = len(cleaned.split())

excl_count = feedback.count("!")

print("\n--- Cleaned Feedback ---")
print("Cleaned text:      ", cleaned)
print("Characters (no !): ", char_count)
print("Words:             ", word_count)
print("Exclamations removed:", excl_count)
