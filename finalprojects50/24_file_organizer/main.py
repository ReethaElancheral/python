# 24. File Organizer 
# Objective: Sort files into folders by extension. 
# Requirements: 
#  File Handling: Move files using os/shutil. 
#  Dictionary: Map extensions to folders ({"jpg": "Images"}). 
#  Exception Handling: Permission errors. 
#  Loops: Process all files in a directory. 
#  Functions: organize(directory). 
#  Generator: Yield files being moved. 
#  Decorator: @dry_run to preview changes.


import os
from organizer.core import organize

def main():
    print("📂 Welcome to File Organizer")
    directory = input("Enter the path of the folder to organize: ").strip()

    if not os.path.isdir(directory):
        print("❌ Invalid directory!")
        return

    confirm = input("Do you want to organize this folder? (yes/dry): ").lower()

    if confirm == "yes":
        from organizer.core import file_generator, move_file, get_extension, EXTENSION_MAP
        for file_path in file_generator(directory):
            try:
                ext = get_extension(file_path)
                folder = EXTENSION_MAP.get(ext, "Others")
                dest_dir = os.path.join(directory, folder)
                move_file(file_path, dest_dir)
                print(f"✅ Moved: {file_path} ➜ {dest_dir}")
            except Exception as e:
                print(f"⚠️ Error moving {file_path}: {e}")
    else:
        organize(directory)

if __name__ == "__main__":
    main()
