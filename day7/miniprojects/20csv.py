# 20. CSV to Sentence Converter

# Concepts: .split(','), .join()
# Input: "apple,banana,cherry"
# Output: "You bought apple, banana, and cherry."


csv_items = input("Enter items (comma-separated): ").strip()

items = [item.strip() for item in csv_items.split(",")]

if len(items) == 0:
    sentence = "You bought nothing."
elif len(items) == 1:
    sentence = f"You bought {items[0]}."
elif len(items) == 2:
    sentence = f"You bought {items[0]} and {items[1]}."
else:
    sentence = f"You bought {', '.join(items[:-1])}, and {items[-1]}."
    
print(sentence)
