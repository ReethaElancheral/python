# 🧩 9. Expense Tracker

# Topics Covered: function list return, sum(), map()
# Requirements:
# Add multiple expenses using *args
# Store in a list and return sum
# Use map() to apply GST (e.g., 18%) on each item

def add_expenses(*expenses):
    expense_list = list(map(float, expenses))
    return expense_list

def total_expenses(expense_list):
    return sum(expense_list)

def apply_gst(expense_list, gst_percent):
    gst_multiplier = 1 + gst_percent / 100
    gst_applied = list(map(lambda x: round(x * gst_multiplier, 2), expense_list))
    return gst_applied


expenses = add_expenses(100, 250.5, 50, 80)
print("Original Expenses:", expenses)

total = total_expenses(expenses)
print("Total without GST:", total)

expenses_with_gst = apply_gst(expenses, 18)
print("Expenses with 18% GST:", expenses_with_gst)

total_with_gst = total_expenses(expenses_with_gst)
print("Total with GST:", total_with_gst)
