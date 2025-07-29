# 23. Random Password Generator 
# Objective: Create secure passwords. 
# Requirements: 
#  String Operations: Concatenate random chars. 
#  List: Pool of characters (["a", "1", "#", ...]). 
#  Functions: generate(length=12). 
#  Loops: Build password string. 
#  Exception Handling: Invalid length. 
#  Generator: Yield infinite passwords. 
#  Decorator: @exclude_similar (e.g., no l/1).


from generator.core import PasswordGenerator

def main():
    print("🔑 Welcome to Random Password Generator")
    generator = PasswordGenerator()

    while True:
        try:
            length_input = input("Enter desired password length (or 'exit'): ").strip()
            if length_input.lower() == 'exit':
                print("Goodbye!")
                break

            length = int(length_input)
            password = generator.generate(length)
            print(f"Generated Password: {password}")

            more = input("Want infinite stream? (y/n): ").lower()
            if more == 'y':
                print("Streaming passwords (press Ctrl+C to stop):")
                stream = generator.password_stream(length)
                for pwd in stream:
                    print(pwd)
        except ValueError as ve:
            print(f"❌ Error: {ve}")
        except KeyboardInterrupt:
            print("\nStream stopped.")
            break

if __name__ == "__main__":
    main()
