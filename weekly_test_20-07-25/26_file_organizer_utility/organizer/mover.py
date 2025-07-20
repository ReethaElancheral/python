import os
import shutil

def move_files_by_type(directory, files_by_type):
    for ext, files in files_by_type.items():
        folder_name = ext if ext else "no_extension"
        dest_folder = os.path.join(directory, folder_name)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        for file in files:
            src = os.path.join(directory, file)
            dest = os.path.join(dest_folder, file)

            try:
                shutil.move(src, dest)
                print(f"Moved: {file} → {folder_name}/")
            except Exception as e:
                print(f"Failed to move {file}: {e}")
