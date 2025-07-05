## 15. Shopping Cart

# - Ask the user to input item names and their prices (3 items).
# - Store items and prices in a dictionary.
# - Calculate and print the total amount.

item1 = input("Enter name of item 1: ")
price1 = float(input(f"Enter price of {item1}: "))

item2 = input("Enter name of item 2: ")
price2 = float(input(f"Enter price of {item2}: "))

item3 = input("Enter name of item 3: ")
price3 = float(input(f"Enter price of {item3}: "))

cart = {
    item1: price1,
    item2: price2,
    item3: price3
}

total = price1 + price2 + price3

print(f"Total amount: {total}")

print(f"{item1}: {price1}")
print(f"{item2}: {price2}")
print(f"{item3}: {price3}")

