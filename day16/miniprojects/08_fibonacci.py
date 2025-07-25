# 8. Fibonacci Sequence Generator 

# Goal: Create a Fibonacci sequence iterator up to n numbers. 
# Requirements: 
#  Use class-based iterator 
#  Raise StopIteration at limit 
#  Print numbers using for loop and manual next() 



class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val

# Usage & Output
fib = FibonacciIterator(7)
print("Fibonacci sequence using for loop:")
for num in fib:
    print(num, end=" ")
print()

fib2 = FibonacciIterator(5)
print("Fibonacci sequence using manual next():")
it = iter(fib2)
try:
    while True:
        print(next(it), end=" ")
except StopIteration:
    print()
