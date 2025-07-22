import os

KEY = 129  # Simple XOR cipher key

def encrypt_file(filepath):
    if not os.path.isfile(filepath):
        print("❌ File does not exist.")
        return

    try:
        with open(filepath, "rb") as file:
            data = file.read()
        encrypted_data = bytes([b ^ KEY for b in data])

        encrypted_path = filepath + ".bin"
        if os.path.exists(encrypted_path):
            print(f"⚠️ Encrypted file already exists: {encrypted_path}")
            return

        with open(encrypted_path, "wb") as file:
            file.write(encrypted_data)
        print(f"✅ File encrypted and saved as: {encrypted_path}")
    except Exception as e:
        print(f"❌ Error during encryption: {e}")

def decrypt_file(filepath):
    if not os.path.isfile(filepath):
        print("❌ File does not exist.")
        return

    if not filepath.endswith(".bin"):
        print("❌ Please provide a .bin encrypted file.")
        return

    try:
        with open(filepath, "rb") as file:
            data = file.read()
        decrypted_data = bytes([b ^ KEY for b in data])

        original_path = filepath[:-4] + "_decrypted"
        if os.path.exists(original_path):
            print(f"⚠️ Decrypted file already exists: {original_path}")
            return

        with open(original_path, "wb") as file:
            file.write(decrypted_data)
        print(f"✅ File decrypted and saved as: {original_path}")
    except Exception as e:
        print(f"❌ Error during decryption: {e}")
