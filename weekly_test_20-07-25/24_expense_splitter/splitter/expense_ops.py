def add_expense(expenses, categories):
    try:
        amount = float(input("Enter expense amount: "))
        payer = input("Enter payer name: ").strip()
        raw_participants = input("Enter participants (comma-separated): ").strip()
        category = input("Enter category: ").strip()

        participants = set(name.strip() for name in raw_participants.split(',') if name.strip())
        if not participants:
            print("No participants entered.")
            return

        expense = {
            "amount": amount,
            "payer": payer,
            "participants": participants,
            "category": category
        }
        expenses.append(expense)
        categories.add(category)
        print(f"Expense added under '{category}' by {payer}.")

    except ValueError:
        print("Invalid amount entered.")

def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n--- Expense List ---")
    for i, e in enumerate(expenses, 1):
        participants_str = ', '.join(e["participants"])
        print(f"{i}. INR {e['amount']:.2f} | Payer: {e['payer']} | Participants: [{participants_str}] | Category: {e['category']}")
