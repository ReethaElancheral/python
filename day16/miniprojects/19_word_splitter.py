# 19. Word Splitter 
# Goal: Use iterators to split a sentence into words and return one word at a time. 
# Requirements: 
#  Use split() + custom iterator 
#  Return one word per next() 
#  End when no more words 

class WordSplitter:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word

# Usage & Output
sentence = "This is a Python iterator example"
print("Words in sentence:")
for word in WordSplitter(sentence):
    print(word)
