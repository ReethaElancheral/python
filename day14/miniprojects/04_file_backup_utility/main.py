from filebackup.operations import create_backup
from filebackup.display import show_banner

def main():
    show_banner()
    source_path = input("Enter the full path of the file to back up: ")
    create_backup(source_path)

if __name__ == "__main__":
    main()
