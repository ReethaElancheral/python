import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choice(char_pool) for _ in range(length))

def generate_multiple_passwords(count=5, length=12, **kwargs):
    return [generate_password(length, **kwargs) for _ in range(count)]
