## 17. Unique Visitor Counter

# - Ask for names of people entering a shop (input, 5 times).
# - Store names in a set.
# - Print the number of unique visitors.


visitor1 = input("Enter name of visitor 1: ")
visitor2 = input("Enter name of visitor 2: ")
visitor3 = input("Enter name of visitor 3: ")
visitor4 = input("Enter name of visitor 4: ")
visitor5 = input("Enter name of visitor 5: ")


unique_visitors = {visitor1, visitor2, visitor3, visitor4, visitor5}

print(f"Number of unique visitors: {len(unique_visitors)}")
