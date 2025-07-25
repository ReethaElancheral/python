# 9. Lazy Square Calculator 

# Goal: Build a lazy square generator using iterators. 
# Requirements: 
#  Accept n numbers from user 
#  Generate squares one at a time 
#  Handle empty list gracefully

class LazySquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        val = self.numbers[self.index]
        self.index += 1
        return val ** 2

# Usage 
user_input = input("Enter numbers separated by space: ").strip()
if not user_input:
    print("Empty input list. No squares to generate.")
else:
    nums = list(map(int, user_input.split()))
    squares = LazySquareIterator(nums)
    print("Squares generated lazily:")
    for sq in squares:
        print(sq, end=" ")
    print()
