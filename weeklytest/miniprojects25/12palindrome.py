# 12. Palindrome Checker

# Concepts: string slicing, functions, loop.
# User inputs a word/sentence.
# Check if it's a palindrome using [::-1].
# Loop for multiple checks.

def is_palindrome(text):

    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

while True:
    user_input = input("Enter a word or sentence to check (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if is_palindrome(user_input):
        print("It's a palindrome ✅")
    else:
        print("Not a palindrome ❌")
