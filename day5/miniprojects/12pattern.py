# ✅ 12. Pattern Printer

# Objective: Print a star pattern using while.
# Requirements:
# Print increasing number of stars:
# Use nested while loop.
# Use pass for lines you want to skip in future.

rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1

    pass
    print()
    i += 1
