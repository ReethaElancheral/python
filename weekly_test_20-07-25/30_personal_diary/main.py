from diary.storage import load_entries, save_entries, add_entry, edit_entry, delete_entry
from diary.search import search_by_tag, search_by_date

def main():
    entries = load_entries()

    while True:
        print("\n📔 Personal Diary Menu:")
        print("1. Add Entry")
        print("2. Edit Entry")
        print("3. Delete Entry")
        print("4. Search by Tag")
        print("5. Search by Date")
        print("6. Show All Entries")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            text = input("Your entry: ").strip()
            tags = set(input("Tags (comma-separated): ").strip().split(","))
            add_entry(entries, date, text, tags)

        elif choice == "2":
            date = input("Date of entry to edit: ").strip()
            edit_entry(entries, date)

        elif choice == "3":
            date = input("Date of entry to delete: ").strip()
            delete_entry(entries, date)

        elif choice == "4":
            tag = input("Enter tag to search: ").strip()
            results = search_by_tag(entries, tag)
            for e in results:
                print(f"\n📅 {e['date']}\n{e['text']}\nTags: {', '.join(e['tags'])}")

        elif choice == "5":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            results = search_by_date(entries, date)
            for e in results:
                print(f"\n📅 {e['date']}\n{e['text']}\nTags: {', '.join(e['tags'])}")

        elif choice == "6":
            for e in entries:
                print(f"\n📅 {e['date']}\n{e['text']}\nTags: {', '.join(e['tags'])}")

        elif choice == "7":
            save_entries(entries)
            print("Diary saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
