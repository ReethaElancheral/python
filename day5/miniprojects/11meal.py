# ✅ 11. Meal Ordering System

# Objective: Simulate food order entry.
# Requirements:
# Use while loop to add items.
# Use break when user types "done".
# Skip empty entries using continue.
# At the end, use else to print total items ordered.

orders = []
while True:
    item = input("Enter a food item (type 'done' to finish): ").strip()
    
    if item == "":
        print("Empty entry skipped.")
        continue
    
    if item.lower() == "done":
        break
    
    orders.append(item)

else:
  
    print("Ordering completed.")

print(f"Total items ordered: {len(orders)}")
print("Items:", ", ".join(orders))
