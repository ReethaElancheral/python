# 15. Text Highlighter 
# Goal: Iterate through a paragraph and yield only capitalized words. 
# Requirements: 
#  Accept multi-line input 
#  Use iterator to return each capitalized word 
#  End gracefully on completion 

class CapitalWordIterator:
    def __init__(self, paragraph):
        self.words = paragraph.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if word.istitle():
                return word
        raise StopIteration

# Usage & Output
para = """Python is a Great language.
Developed by Guido Van Rossum.
Used in Data Science and Web."""

print("Capitalized words:")
for word in CapitalWordIterator(para):
    print(word)
