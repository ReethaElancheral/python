# 18. Prime Number Streamer 
# Objective: Generate prime numbers up to N lazily. 
# Requirements: 
#  Use generator with efficient prime check. 
#  Skip even numbers after 2. 
#  Stop using StopIteration. 

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def prime_stream(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Example usage:
for prime in prime_stream(30):
    print(prime)
