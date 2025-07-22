from encryptor.operations import encrypt_file, decrypt_file
from encryptor.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            path = input("Enter path of file to encrypt: ").strip()
            encrypt_file(path)
        elif choice == '2':
            path = input("Enter path of file to decrypt: ").strip()
            decrypt_file(path)
        elif choice == '3':
            print("Exiting Encryption Tool.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
