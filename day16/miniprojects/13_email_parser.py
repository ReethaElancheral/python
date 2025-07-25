# 13. Email Parser 

# Goal: Iterate through lines of emails and yield only valid email addresses. 
# Requirements: 
#  Validate email format 
#  Use yield + custom class or function 
#  Stop at StopIteration 

import re

class EmailIterator:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.email_regex = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            match = self.email_regex.search(line)
            if match:
                return match.group()
        raise StopIteration

# Usage & Output
lines = [
    "Hello user1@example.com",
    "Invalid line",
    "Contact us at help@support.org",
    "No email here"
]
print("Valid emails found:")
for email in EmailIterator(lines):
    print(email)
