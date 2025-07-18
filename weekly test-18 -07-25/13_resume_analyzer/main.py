from analyzer.resume_analyzer import add_resume, view_resumes

def main():
    database = {}

    while True:
        print("\n1. Add Resume")
        print("2. View Analyzed Resumes")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            aid = input("Enter Applicant ID: ").strip()
            print("Paste resume content (one line):")
            resume = input()
            add_resume(aid, resume, database)

        elif choice == "2":
            view_resumes(database)

        elif choice == "3":
            print("Exiting Resume Analyzer.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
