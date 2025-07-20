from collections import defaultdict

def category_summary(expenses):
    totals = defaultdict(float)
    for _, category, amount in expenses:
        totals[category] += amount
    print("\n--- Category-wise Summary ---")
    for cat, amt in totals.items():
        print(f"{cat}: ₹{amt}")

def monthly_summary(expenses):
    monthly = defaultdict(float)
    for date, _, amount in expenses:
        month = date[:7]  # YYYY-MM
        monthly[month] += amount
    print("\n--- Monthly Summary ---")
    for m, amt in monthly.items():
        print(f"{m}: ₹{amt}")

def unique_categories(expenses):
    return set(category for _, category, _ in expenses)
