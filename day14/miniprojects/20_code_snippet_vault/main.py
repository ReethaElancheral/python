from vault.snippet_manager import add_snippet, search_snippets_by_title, search_snippets_by_tag
from vault.display import show_menu

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_snippet()
        elif choice == '2':
            search_snippets_by_title()
        elif choice == '3':
            search_snippets_by_tag()
        elif choice == '4':
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
