# 4. Secure File Reader

# Use Case: Read and display content from a user-given file. 
# Exception Handling Goals:
# Handle FileNotFoundError
# Raise PermissionError if file not readable
# Use finally to ensure file is closed
# Log all file errors
# Nested try block for open/read operations

import os
import logging

# Setup logging
logging.basicConfig(filename="file_reader_errors.log", level=logging.ERROR)

def secure_file_read():
    file_path = input("Enter the path of the file to read: ")
    file = None

    try:
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"No such file: {file_path}")

            if not os.access(file_path, os.R_OK):
                raise PermissionError(f"File exists but is not readable: {file_path}")

            file = open(file_path, 'r')
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)

        except FileNotFoundError as fnf:
            logging.error(fnf, exc_info=True)
            print(f"❌ Error: {fnf}")

        except PermissionError as pe:
            logging.error(pe, exc_info=True)
            print(f"❌ Error: {pe}")

        except Exception as e:
            logging.error(f"Unexpected error: {e}", exc_info=True)
            print(f"❌ Unexpected error occurred: {e}")

    finally:
        if file:
            file.close()
            print("✅ File closed.")
        else:
            print("ℹ️ No file was opened.")


if __name__ == "__main__":
    secure_file_read()
