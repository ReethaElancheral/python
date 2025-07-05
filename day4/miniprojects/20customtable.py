# ✅ 20. Custom Size Multiplication Table

# Objective: Print a dynamic multiplication table using nested loops.
# Requirements:
# Input: table size (e.g., 5x5 or 10x10).
# Outer loop: rows
# Inner loop: columns
# Use print(f"{i} x {j} = {i*j}").


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nMultiplication Table:")

for i in range(1, rows + 1):

    for j in range(1, cols + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
