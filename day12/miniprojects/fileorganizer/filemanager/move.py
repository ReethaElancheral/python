import os
import shutil

def move_files(file_dict, base_path):
    moved_files = {}

    for category, files in file_dict.items():
        category_folder = os.path.join(base_path, category)
        os.makedirs(category_folder, exist_ok=True)

        moved_files[category] = []

        for file in files:
            try:
                filename = os.path.basename(file)
                target_path = os.path.join(category_folder, filename)
                shutil.move(file, target_path)
                moved_files[category].append(filename)
            except Exception as e:
                print(f"Error moving {file}: {e}")
    return moved_files
