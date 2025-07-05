# ✅ 8. Number Type Analyzer

# Objective: Analyze even/odd, positive/negative.
# Requirements:
# Input a list of numbers.
# Use for loop + if to print:
# Even/Odd
# Positive/Negative

numbers_input = input("Enter numbers separated by commas: ").split(',')

numbers = [int(num.strip()) for num in numbers_input]

print("\n🔎 Number Analysis:")
for num in numbers:

    if num % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"
    
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    print(f"{num} → {even_odd}, {sign}")
