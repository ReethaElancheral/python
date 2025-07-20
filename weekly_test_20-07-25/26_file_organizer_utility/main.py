import os
from organizer.scanner import scan_directory
from organizer.mover import move_files_by_type

def main():
    target_dir = input("Enter the path to the directory you want to organize: ").strip()

    if not os.path.isdir(target_dir):
        print("Invalid directory path.")
        return

    file_map = scan_directory(target_dir)

    print("\nFile types found:")
    for ext in sorted(file_map):
        print(f"{ext if ext else '[No Extension]'}: {len(file_map[ext])} file(s)")

    confirm = input("\nDo you want to organize these files into folders? (y/n): ").lower()
    if confirm == 'y':
        move_files_by_type(target_dir, file_map)
        print("Files organized successfully.")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
