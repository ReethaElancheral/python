from explorer.metadata import scan_folder_and_export
from explorer.display import welcome_banner

def main():
    welcome_banner()
    folder = input("📂 Enter the folder path to scan: ").strip()
    scan_folder_and_export(folder)

if __name__ == "__main__":
    main()
