# 11. Digit Extractor from String 

# Goal: Extract digits from a mixed string using a custom iterator. 
# Requirements: 
#  Input: "abc123def456" 
#  Output: 1, 2, 3, 4, 5, 6 
#  Stop when no more digits 

class DigitExtractor:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            ch = self.text[self.index]
            self.index += 1
            if ch.isdigit():
                return int(ch)
        raise StopIteration



s = "abc123def456"
print("Digits extracted:")
for d in DigitExtractor(s):
    print(d, end=" ")
print()
