# ✅ 1. Grocery List Formatter

# Objective: Format and print a list of grocery items using for loop and enumerate().
# Requirements:
# Accept a list of grocery items (e.g., milk, eggs, rice).
# Print each item with a serial number (starting from 1).
# Use enumerate() with start=1.


items_input = input("Enter grocery items separated by commas: ")

grocery_items = [item.strip() for item in items_input.split(",")]

print("\nGrocery List:")
for index, item in enumerate(grocery_items, start=1):
    print(f"{index}. {item}")
