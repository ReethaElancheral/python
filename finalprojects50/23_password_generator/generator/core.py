import random
import string

# Decorator to exclude similar characters like 'l', '1', 'I', 'O', '0'
def exclude_similar(func):
    def wrapper(*args, **kwargs):
        password = func(*args, **kwargs)
        similar_chars = {'l', '1', 'I', 'O', '0'}
        while any(char in similar_chars for char in password):
            password = func(*args, **kwargs)
        return password
    return wrapper

class PasswordGenerator:
    def __init__(self):
        self.char_pool = list(
            string.ascii_letters + string.digits + string.punctuation
        )
        self.similar_chars = {'l', '1', 'I', 'O', '0'}

    @exclude_similar
    def generate(self, length=12):
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer.")
        return ''.join(random.choice(self.char_pool) for _ in range(length))

    def password_stream(self, length=12):
        while True:
            yield self.generate(length)
