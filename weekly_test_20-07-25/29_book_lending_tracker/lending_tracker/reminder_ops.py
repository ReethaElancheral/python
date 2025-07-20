from datetime import datetime

def check_overdue(books):
    today = datetime.today().date()
    found = False
    print("\n📅 Overdue Books:")
    for title, (borrower, due_date_str) in books.items():
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if due_date < today:
                print(f"- {title} borrowed by {borrower} (Due: {due_date})")
                found = True
        except ValueError:
            print(f"- Invalid date format for '{title}'.")
    if not found:
        print("No overdue books.")
