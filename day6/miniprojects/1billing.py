# 🧩 1. Billing System

# Topics Covered: def, *args, return, local/global variables
# Requirements:
# Add items with price
# Calculate total using a function
# Apply discount with a function
# Use *args to allow multiple item prices
# Use global variable to maintain the total bill


total_bill = 0

def add_items(*prices):
    global total_bill
    for price in prices:
        total_bill += price
    print(f"Items added. Current total: ₹{total_bill}")

def apply_discount(percent):
    global total_bill
    discount_amount = (percent / 100) * total_bill
    total_bill -= discount_amount
    print(f"Discount of {percent}% applied. New total: ₹{total_bill:.2f}")

def get_total():
    return total_bill

add_items(100, 250, 50)   
add_items(500)            
apply_discount(10)        
print("Final Total: ₹", get_total()) 