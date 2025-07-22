from renamer.rename_util import rename_txt_files
from renamer.display import show_banner

def main():
    show_banner()
    folder_path = input("Enter folder path to rename .txt files: ").strip()
    rename_txt_files(folder_path)

if __name__ == "__main__":
    main()
