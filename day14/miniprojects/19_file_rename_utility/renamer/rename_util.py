import os

def rename_txt_files(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    if not txt_files:
        print("No .txt files found in the folder.")
        return

    existing_files = set(os.listdir(folder_path))
    count = 1
    for old_name in txt_files:
        new_name = f"file_{count}.txt"
        while new_name in existing_files:
            count += 1
            new_name = f"file_{count}.txt"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{old_name}' to '{new_name}'")
        existing_files.add(new_name)
        count += 1
