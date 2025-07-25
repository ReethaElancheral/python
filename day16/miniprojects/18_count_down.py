# 18. Countdown Timer
#  
# Goal: Simulate a countdown using an iterator. 
# Requirements: 
#  Start from user input (e.g. 5) 
#  Print 5...4...3...2...1 
#  Raise StopIteration at 0

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Usage & Output
start = 5
print(f"Countdown from {start}:")
for num in Countdown(start):
    print(num, end="...")
