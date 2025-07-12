# 22. Message Encoder/Decoder

# Concepts: strings, list, loop, functions.
# Convert message to ASCII or reverse.
# Option for encoding/decoding.
# Use loop to process character-wise.



def encode_message(message):
    encoded = []
    for char in message:
        encoded.append(str(ord(char)))  
    return ' '.join(encoded)

def decode_message(code):
    decoded = []
    parts = code.strip().split()
    for ascii_val in parts:
        if ascii_val.isdigit():
            decoded.append(chr(int(ascii_val)))  
        else:
            decoded.append('?') 
    return ''.join(decoded)


while True:
    print("\n=== Message Encoder/Decoder ===")
    print("1. Encode message to ASCII")
    print("2. Decode ASCII to message")
    print("3. Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        msg = input("Enter your message to encode: ")
        encoded = encode_message(msg)
        print(f"Encoded ASCII: {encoded}")

    elif choice == "2":
        code = input("Enter ASCII codes separated by space: ")
        decoded = decode_message(code)
        print(f"Decoded Message: {decoded}")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
