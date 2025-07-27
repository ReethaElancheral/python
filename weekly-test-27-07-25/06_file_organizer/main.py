import os
from organizer.organize import organize_by_extension
from organizer.duplicates import find_and_remove_duplicates
from organizer.rename import bulk_rename
from organizer.largest import find_largest_files
from organizer.scheduler import schedule_organization

def main():
    print("File Organizer App")
    folder = input("Enter folder path to manage: ").strip()

    if not os.path.isdir(folder):
        print("Invalid folder path.")
        return

    while True:
        print("\nMenu:")
        print("1. Organize files by extension")
        print("2. Remove duplicate files")
        print("3. Bulk rename files")
        print("4. Find largest files")
        print("5. Schedule automatic organization (every 60 sec)")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            organize_by_extension(folder)

        elif choice == "2":
            find_and_remove_duplicates(folder)

        elif choice == "3":
            pattern = input("Enter regex pattern to find: ")
            replacement = input("Enter replacement string: ")
            bulk_rename(folder, pattern, replacement)

        elif choice == "4":
            try:
                count = int(input("How many largest files to list? "))
            except ValueError:
                count = 5
            find_largest_files(folder, count)

        elif choice == "5":
            print("Scheduling organization every 60 seconds...")
            schedule_organization(folder, 60)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
