# ✅ 11. Triangle Number Pattern App

# Objective: Create a number pattern like:
# CopyEdit1  
# 1 2  
# 1 2 3  

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
