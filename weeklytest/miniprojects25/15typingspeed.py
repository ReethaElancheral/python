# 15. Typing Speed Test

# Concepts: string methods, while, lists, functions.
# Show a sentence.
# Record typing and compare.
# Calculate time taken, errors.
# Use split() and string comparison.

import time

def typing_test(sentence):
    print("\nType the following sentence exactly:")
    print(sentence)
    input("Press Enter when ready...")

    start_time = time.time()
    typed = input("Start typing:\n")
    end_time = time.time()

    time_taken = end_time - start_time  
    time_taken_minutes = time_taken / 60  


    original_words = sentence.split()
    typed_words = typed.split()


    errors = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] != typed_words[i]:
            errors += 1
    errors += abs(len(original_words) - len(typed_words))

 
    wpm = len(typed_words) / time_taken_minutes if time_taken_minutes > 0 else 0

    accuracy = max(0, (len(original_words) - errors) / len(original_words) * 100)

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Errors made: {errors}")
    print(f"Your typing accuracy: {accuracy:.2f}%")
    print(f"Your typing speed: {wpm:.2f} WPM")


sentence = "The quick brown fox jumps over the lazy dog."


while True:
    typing_test(sentence)
    again = input("\nTry again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for testing your typing speed!")
        break

