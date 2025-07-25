# 1. Custom Range Generator 

# Goal: Create a custom iterator class MyRange(start, end) that behaves like the 
# built-in range. 
# Requirements: 
#  Implement __iter__() and __next__() 
#  Use StopIteration to terminate 
#  Reuse iterator multiple times 

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # Return a new iterator instance to allow multiple reuse
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val


print("MyRange output:")
r = MyRange(3, 8)
for num in r:
    print(num, end=" ")
print()

# Reusing the iterator multiple times
print("Reusing MyRange:")
for num in r:
    print(num, end=" ")
print()



