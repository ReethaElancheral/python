import sys
import os
from filemanager import scan, move, report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <folder_path>")
        return

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    print(f"Scanning folder: {folder_path}")
    categorized = scan.scan_directory(folder_path)

    print("Moving files into categories...")
    moved = move.move_files(categorized, folder_path)

    report.generate_report(moved)

if __name__ == "__main__":
    main()
