# 4. Even-Odd Splitter

# Goal: Design a dual iterator system: one yields even numbers, another odd 
# numbers from a list. 
# Requirements: 
#  Implement two classes 
#  Use __iter__() and __next__() 
#  Handle exhausted iterators using StopIteration 

class EvenIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            if val % 2 == 0:
                return val
        raise StopIteration

class OddIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            if val % 2 != 0:
                return val
        raise StopIteration

# Usage & Output
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("Even numbers:")
for even in EvenIterator(nums):
    print(even, end=" ")
print("\nOdd numbers:")
for odd in OddIterator(nums):
    print(odd, end=" ")
print()
