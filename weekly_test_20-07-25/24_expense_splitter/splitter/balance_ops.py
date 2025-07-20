def calculate_balances(expenses):
    balances = {}

    for e in expenses:
        amount = e['amount']
        payer = e['payer']
        participants = e['participants']
        split = amount / len(participants)

        for person in participants:
            balances[person] = balances.get(person, 0) - split
        balances[payer] = balances.get(payer, 0) + amount

    return balances

def show_balances(balances):
    print("\n--- Current Balances ---")
    if not balances:
        print("No balances to show.")
        return

    for person, balance in balances.items():
        status = "owes" if balance < 0 else "gets"
        print(f"{person}: {status} INR {abs(balance):.2f}")
