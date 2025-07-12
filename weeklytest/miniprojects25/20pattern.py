# 20. Pattern Generator

# Concepts: while loop, string operations.
# Print star, triangle, number patterns.
# User chooses type and size.
# Use nested loops.

def star_pattern(size):
    print("\nStar Pattern:")
    for i in range(1, size + 1):
        print("* " * i)

def triangle_pattern(size):
    print("\nTriangle Pattern:")
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)

def number_pattern(size):
    print("\nNumber Pattern:")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern_generator():
    while True:
        print("\n--- Pattern Generator Menu ---")
        print("1. Star Pattern")
        print("2. Triangle Pattern")
        print("3. Number Pattern")
        print("4. Exit")

        choice = input("Choose a pattern (1-4): ").strip()

        if choice == "4":
            print("Exiting Pattern Generator. Goodbye!")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid choice, please select from 1 to 4.")
            continue

        size_input = input("Enter pattern size (positive integer): ").strip()
        if not size_input.isdigit() or int(size_input) <= 0:
            print("Invalid size. Please enter a positive integer.")
            continue
        size = int(size_input)

        if choice == "1":
            star_pattern(size)
        elif choice == "2":
            triangle_pattern(size)
        elif choice == "3":
            number_pattern(size)

pattern_generator()
