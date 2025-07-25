# 2. Reverse String Iterator 

# Goal: Build an iterator that returns characters of a string in reverse order. 
# Requirements: 
#  Accept input string dynamically 
#  Use __next__() to return one character at a time 
#  Validate empty string using exception

class ReverseStringIterator:
    def __init__(self, text):
        if not text:
            raise ValueError("Empty string is not allowed")
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.text[self.index]
        self.index -= 1
        return char


try:
    rev_iter = ReverseStringIterator("Hello")
    print("Reverse String Iterator output:")
    for ch in rev_iter:
        print(ch, end="")
    print()
    
    # Testing empty string exception
    print("Testing empty string input:")
    empty_iter = ReverseStringIterator("")
except ValueError as e:
    print("Error:", e)
