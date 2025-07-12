# 21. Library Due Date Calculator

# Concepts: string formatting, list, functions.
# Input book name, borrow date.
# Calculate due date (assume +7 days).
# Display summary.

from datetime import datetime, timedelta

records = [] 

def valid_date(date_str):
  
    if len(date_str) != 10:
        return False
    if date_str[4] != '-' or date_str[7] != '-':
        return False
    y, m, d = date_str.split('-')
    if not (y.isdigit() and m.isdigit() and d.isdigit()):
        return False
    try:
        datetime(int(y), int(m), int(d))
        return True
    except:
        return False

def calculate_due_date(borrow_date):
    dt = datetime.strptime(borrow_date, "%Y-%m-%d")
    due = dt + timedelta(days=7)
    return due.strftime("%Y-%m-%d")

def add_record():
    book_name = input("Enter book name: ").strip()
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ").strip()
    if not valid_date(borrow_date):
        print("Invalid date format or invalid date. Please try again.")
        return
    due_date = calculate_due_date(borrow_date)
    records.append([book_name, borrow_date, due_date])
    print(f"Record added: '{book_name}' borrowed on {borrow_date}, due on {due_date}.")

def show_records():
    if not records:
        print("No records available.")
        return
    print("\n--- Library Borrow Records ---")
    print(f"{'Book Name':<30} {'Borrow Date':<12} {'Due Date':<12}")
    for book, borrow, due in records:
        print(f"{book:<30} {borrow:<12} {due:<12}")

while True:
    print("\nLibrary Due Date Calculator Menu:")
    print("1. Add borrow record")
    print("2. Show all records")
    print("3. Exit")

    choice = input("Choose an option (1-3): ").strip()
    if choice == "1":
        add_record()
    elif choice == "2":
        show_records()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 3.")
