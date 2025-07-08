# ✅ 5. Multiplication Table Generator

# Objective: Display multiplication table for any number.
# Requirements:
# Input: number
# Use a while loop to print table from 1 to 10.
# Use else to say “Table completed”.

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
else:
    print("Table completed ✅")
