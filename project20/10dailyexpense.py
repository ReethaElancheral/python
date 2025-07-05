# ✅ 10. Daily Expense Tracker

# Objective: Track expenses and suggest savings.
# Requirements:
# Input 7 daily expenses using a list.
# Use for loop to sum total.
# If total > 3000 → print “Cut down on expenses”.

expenses = []
print("Enter your expenses for 7 days:")

for day in range(1, 8):
    amount = float(input(f"Day {day}: ₹"))
    expenses.append(amount)

total = sum(expenses)

print(f"\nTotal Expenses: ₹{total:.2f}")

if total > 3000:
    print("⚠️ Cut down on expenses!")
else:
    print("👍 Your expenses are within budget.")
