# ✅ 13. Reverse Counter App

# Objective: Count down from any number to 1.
# Requirements:
# Input: starting number
# Use while loop to count down.
# Stop if number becomes zero using break.

start_num = int(input("Enter the starting number: "))

while True:
    if start_num == 0:
        break
    print(start_num)
    start_num -= 1
