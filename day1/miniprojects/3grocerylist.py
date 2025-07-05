## 3. Grocery List

# - Let the user input three grocery items (using input()).
# - Store them in a list.
# - Print the items, separated by commas (using sep).
# - Show the type of the list variable.

item1 = input("Enter first Grocery:" )
item2 = input("Enter second Grocery:" )
item3 = input("Enter third Grocery:" )

grocery_list = [item1, item2, item3]

print(*grocery_list, sep=",")

print('Type of grocery list variable are:', type(grocery_list))

