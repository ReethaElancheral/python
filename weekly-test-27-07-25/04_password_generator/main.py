from password_gen.generator import generate_multiple_passwords
from password_gen.strength import password_strength
from password_gen.file_handler import save_passwords, load_passwords

def get_bool_input(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"

def main():
    while True:
        print("\n=== Password Generator ===")
        print("1. Generate Passwords")
        print("2. View Saved Passwords")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            count = int(input("How many passwords to generate? "))
            length = int(input("Length of each password? "))
            use_upper = get_bool_input("Include uppercase letters?")
            use_lower = get_bool_input("Include lowercase letters?")
            use_digits = get_bool_input("Include numbers?")
            use_symbols = get_bool_input("Include symbols?")

            passwords = generate_multiple_passwords(
                count=count,
                length=length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_symbols=use_symbols
            )

            for i, pwd in enumerate(passwords, 1):
                strength = password_strength(pwd)
                print(f"{i}. {pwd}  →  Strength: {strength}")

            if get_bool_input("Save passwords to encrypted file?"):
                save_passwords(passwords)
                print("Passwords saved securely.")

        elif choice == "2":
            try:
                passwords = load_passwords()
                print("\nSaved Passwords:")
                for i, pwd in enumerate(passwords, 1):
                    print(f"{i}. {pwd}")
            except Exception as e:
                print(f"Error reading saved passwords: {e}")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
