from resumes.collector import add_resume, search_resume, update_resume
from resumes.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Add Resume")
        print("2. Search Resume")
        print("3. Update Resume")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_resume()
        elif choice == '2':
            search_resume()
        elif choice == '3':
            update_resume()
        elif choice == '4':
            print("Exiting Resume Collector.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
