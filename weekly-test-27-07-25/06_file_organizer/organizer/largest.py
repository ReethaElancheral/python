import os

def find_largest_files(folder_path, count=5):
    all_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                all_files.append((filepath, size))
            except Exception as e:
                print(f"Error accessing {filepath}: {e}")

    all_files.sort(key=lambda x: x[1], reverse=True)

    print(f"Top {count} largest files:")
    for filepath, size in all_files[:count]:
        print(f"{filepath} - {size / (1024*1024):.2f} MB")
