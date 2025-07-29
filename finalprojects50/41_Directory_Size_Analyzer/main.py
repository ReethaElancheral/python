import os
from pathlib import Path
from functools import wraps

def human_readable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        size_bytes = func(*args, **kwargs)
        if size_bytes is None:
            return None
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
    return wrapper

class DirectorySizeAnalyzer:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        if not self.root_path.exists() or not self.root_path.is_dir():
            raise ValueError(f"{root_path} is not a valid directory.")
        self.sizes = {}

    @human_readable
    def get_dir_size(self, path):
        total_size = 0
        try:
            for entry in os.scandir(path):
                if entry.is_file():
                    total_size += entry.stat().st_size
                elif entry.is_dir():
                    total_size += self.get_dir_size(entry.path)
        except PermissionError:
            print(f"Permission denied: {path}")
        return total_size

    def analyze(self):
        print(f"Analyzing sizes under: {self.root_path}")
        for root, dirs, files in os.walk(self.root_path):
            size = self.get_dir_size(root)
            self.sizes[root] = size

    def get_large_files(self, threshold_bytes):
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                filepath = Path(root) / file
                try:
                    size = filepath.stat().st_size
                    if size >= threshold_bytes:
                        yield filepath, size
                except PermissionError:
                    print(f"Permission denied: {filepath}")

def main():
    print("Directory Size Analyzer")
    path = input("Enter directory path to analyze: ").strip()
    try:
        analyzer = DirectorySizeAnalyzer(path)
    except ValueError as e:
        print(e)
        return

    analyzer.analyze()
    print("\nFolder sizes:")
    for folder, size in analyzer.sizes.items():
        print(f"{folder}: {size}")

    threshold_mb = input("\nShow files larger than (MB, enter 0 to skip): ").strip()
    try:
        threshold_bytes = int(float(threshold_mb) * 1024 * 1024)
    except ValueError:
        print("Invalid number. Exiting.")
        return

    if threshold_bytes > 0:
        print(f"\nFiles larger than {threshold_mb} MB:")
        for filepath, size in analyzer.get_large_files(threshold_bytes):
            size_hr = size
            # Convert size to human readable
            size_hr = size
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_hr < 1024:
                    size_hr = f"{size_hr:.2f} {unit}"
                    break
                size_hr /= 1024
            print(f"{filepath}: {size_hr}")

if __name__ == "__main__":
    main()
