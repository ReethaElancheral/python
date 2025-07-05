# ✅ 18. Prime Number Finder (1–50)

# Objective: Find all prime numbers between 1 and 50.
# Requirements:
# Use nested loops.
# Use a flag variable to check divisibility.
# If no divisor found → prime.

print("Prime numbers between 1 and 50:")

for num in range(2, 51):  
    is_prime = True     

    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            is_prime = False  

    if is_prime:
        print(num, end=" ")
