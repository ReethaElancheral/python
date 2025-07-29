# 12. Hangman Game 
# Objective: Guess the word before running out of attempts. 
# Requirements: 
#  OOP: Hangman class (word, attempts, guessed_letters). 
#  String Operations: Display word with blanks (e.g., _ _ _ _). 
#  List: Track guessed letters. 
#  File Handling: Load words from a text file. 
#  Exception Handling: Invalid input (non-alphabet). 
#  Conditionals: Check if letter is in word. 
#  Loops: Continue until win/lose. 
#  Generator: Yield hints after 3 failed attempts. 
#  Decorator: @validate_input for letter guesses.

from hangman.core import Hangman

def main():
    print("🎮 Welcome to the CLI Hangman Game!")
    game = Hangman()

    hint_gen = game.hint_generator()

    while True:
        game.display_word()
        guess = input("Guess a letter: ").strip()
        valid = game.guess_letter(guess)
        if not valid:
            continue

        if game.is_won():
            print(f"🎉 Congratulations! You guessed the word: '{game.word}'")
            break

        if game.failed_attempts >= 3:
            try:
                print(next(hint_gen))
            except StopIteration:
                pass

        if game.is_lost():
            print(f"😞 Game over! The word was: '{game.word}'")
            break

if __name__ == "__main__":
    main()
