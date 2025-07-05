# ✅ 14. Restaurant Bill Splitter

# Objective: Split total bill among friends.
# Requirements:
# Input: prices of food items (list).
# Use loop to calculate total.
# Input number of friends → split amount using division.

prices_input = input("Enter prices of food items (comma-separated): ").split(',')

prices = [float(price.strip()) for price in prices_input]

total = sum(prices)
print(f"\nTotal Bill: ₹{total:.2f}")

friends = int(input("Enter number of friends to split bill: "))

if friends > 0:
    split_amount = total / friends
    print(f"Each friend pays: ₹{split_amount:.2f}")
else:
    print("Number of friends should be greater than zero.")
