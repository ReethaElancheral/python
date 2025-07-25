# 12. Skip and Pick Iterator 

# Goal: Design an iterator that skips every alternate item in a list. 
# Requirements: 
#  Custom class with __next__() 
#  Skip logic using index 
#  Works on any list

class SkipAndPickIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        self.index += 2  # Skip alternate
        return value

items = ['a', 'b', 'c', 'd', 'e']
print("Picked items:")
for val in SkipAndPickIterator(items):
    print(val, end=" ")
