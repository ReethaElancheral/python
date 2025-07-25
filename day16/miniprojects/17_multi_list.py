# 17. Multi-List Iterator 
# Goal: Create a class that can iterate over two lists as one. 
# Requirements: 
#  Accept two lists 
#  Combine and iterate over both 
#  StopIteration when both are done 

class MultiListIterator:
    def __init__(self, list1, list2):
        self.combined = list1 + list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.combined):
            raise StopIteration
        val = self.combined[self.index]
        self.index += 1
        return val

# Usage & Output
a = [1, 2, 3]
b = ['a', 'b', 'c']
print("Combined iteration:")
for item in MultiListIterator(a, b):
    print(item, end=" ")
