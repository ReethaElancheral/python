import json
import os
from functools import wraps

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

HISTORY_FILE = "morse_history.json"

def log_translation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Log input and output
        log = {
            "function": func.__name__,
            "input": args[0] if args else "",
            "output": result
        }
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r") as f:
                    history = json.load(f)
            except:
                history = []
        else:
            history = []
        history.append(log)
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=4)
        return result
    return wrapper

class MorseCodeTranslator:

    @staticmethod
    @log_translation
    def encode(text):
        try:
            text = text.upper()
            encoded = []
            for char in text:
                if char not in MORSE_CODE_DICT:
                    raise ValueError(f"Character '{char}' cannot be translated to Morse.")
                encoded.append(MORSE_CODE_DICT[char])
            return ' '.join(encoded)
        except ValueError as e:
            return str(e)

    @staticmethod
    @log_translation
    def decode(morse_code):
        try:
            words = morse_code.strip().split(' / ')
            decoded_words = []
            for word in words:
                chars = word.strip().split()
                decoded_chars = []
                for code in chars:
                    if code not in REVERSE_MORSE_DICT:
                        raise ValueError(f"Morse code '{code}' is invalid.")
                    decoded_chars.append(REVERSE_MORSE_DICT[code])
                decoded_words.append(''.join(decoded_chars))
            return ' '.join(decoded_words)
        except ValueError as e:
            return str(e)

    def generator_encode(self, texts):
        for text in texts:
            yield self.encode(text)

    def generator_decode(self, morse_codes):
        for code in morse_codes:
            yield self.decode(code)

def main():
    translator = MorseCodeTranslator()

    print("Morse Code Translator CLI")
    print("Options:\n1. Encode Text to Morse\n2. Decode Morse to Text\n3. Exit")

    while True:
        choice = input("Choose option (1/2/3): ").strip()
        if choice == '1':
            text = input("Enter text to encode: ").strip()
            if not text:
                print("Empty input. Try again.")
                continue
            result = translator.encode(text)
            print(f"Encoded Morse:\n{result}")
        elif choice == '2':
            morse_code = input("Enter Morse code to decode (use spaces between letters and '/' between words): ").strip()
            if not morse_code:
                print("Empty input. Try again.")
                continue
            result = translator.decode(morse_code)
            print(f"Decoded Text:\n{result}")
        elif choice == '3':
            print("Exiting Morse Code Translator.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
