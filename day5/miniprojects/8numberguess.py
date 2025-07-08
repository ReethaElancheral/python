# ✅ 8. Number Guessing Game

# Objective: Guess a secret number.
# Requirements:
# Use while loop to ask for guesses.
# Use if to check guess.
# Use break if correct.
# Use else block if guess was never correct in 5 tries.

secret_number = 7
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Guess the number: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
else:
    print("Sorry, you didn't guess the number in 5 tries.")
