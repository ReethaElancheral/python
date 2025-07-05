# ✅ 5. Pattern Printer App

# Objective: Print a right-angled triangle star pattern using nested loops.
# Requirements:
# Input: number of rows.
# Use nested for loop:
# Outer loop for rows
# Inner loop for printing *
# Use print("*", end=" ") and print() properly.


rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end=" ")
    print()  


