# 12. Number Guessing Game

# Use Case: User guesses a random number. 
# Exception Handling Goals:
# Catch non-numeric guesses
# Raise GameOverError after 5 failed attempts
# Use try-except-finally for turn logic

import random

# Custom Exception
class GameOverError(Exception):
    pass

def number_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number (1-20): ")
            guess_num = int(guess)
            if guess_num < 1 or guess_num > 20:
                print("❌ Please guess a number between 1 and 20.")
                continue
            if guess_num == secret_number:
                print("🎉 Correct! You guessed the number!")
                break
            else:
                print("❌ Wrong guess, try again.")
                attempts += 1
                if attempts == max_attempts:
                    raise GameOverError("Maximum attempts reached. Game Over!")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")
        except GameOverError as goe:
            print(f"🚫 {goe}")
            break
        finally:
            print("➡️ Turn complete.\n")

if __name__ == "__main__":
    number_guessing_game()
