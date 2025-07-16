# 4. Daily Expense Tracker

# Description: Track your daily expenses.
# Requirements:
# - Structure: {date: {"food": amt, "transport": amt, "misc": amt}}
# - Calculate daily and monthly total
# - Filter days with highest spending
# - Use update(), copy() to replicate structure for new month
# - Use dictionary comprehension to extract days with food > 200


expenses = {
    "2025-07-01": {"food": 150, "transport": 80, "misc": 40},
    "2025-07-02": {"food": 250, "transport": 60, "misc": 30},
    "2025-07-03": {"food": 180, "transport": 90, "misc": 70},
    "2025-07-04": {"food": 220, "transport": 50, "misc": 60}
}


daily_totals = {date: sum(categories.values()) for date, categories in expenses.items()}
total_month = sum(daily_totals.values())


max_spend = max(daily_totals.values(), default=0)
highest_days = [d for d, t in daily_totals.items() if t == max_spend]


next_month = { **expenses } 
next_month.update({"2025-08-01": {"food": 200, "transport": 70, "misc": 50}})


high_food = {d: info["food"] for d, info in expenses.items() if info["food"] > 200}

print("Daily Totals:", daily_totals)
print("Monthly Total: ₹", total_month)

print("Highest Spending Days:", highest_days)

print("\nNext Month Sample:", next_month)

print("\nDays with food > 200:", high_food)
