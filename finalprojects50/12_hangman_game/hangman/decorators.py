import functools

def validate_input(func):
    @functools.wraps(func)
    def wrapper(self, letter):
        if not letter.isalpha() or len(letter) != 1:
            print("⚠️ Invalid input! Please enter a single alphabetic letter.")
            return False
        return func(self, letter.lower())
    return wrapper
