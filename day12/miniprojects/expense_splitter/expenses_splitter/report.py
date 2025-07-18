def print_report(members, total, share):
    print(f"\nTotal Expense: ${total}")
    print(f"Each should pay: ${share}\n")

    for member in members:
        status = "owes" if member['owed'] > 0 else "gets back"
        amount = abs(member['owed'])
        print(f"{member['name']} {status} ${amount}")
