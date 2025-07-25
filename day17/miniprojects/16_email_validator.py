# 16. Email Validator 
# Objective: Validate emails from a list using generators. 
# Requirements: 
#  Use yield to lazily process. 
#  Use regex inside generator expression. 
#  Stop when 10 valid emails are found. 

import re

def email_validator(emails):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    count = 0
    for email in emails:
        if pattern.match(email):
            yield email
            count += 1
        if count == 10:
            break

# Example usage:
emails = [
    "john@example.com", "invalid@", "nisha@domain.in", "test@.com",
    "user@abc.org", "hello@gmail", "valid123@site.com", "check@domain.com",
    "foo@bar.com", "wrong@", "yep@real.co", "yes@try.in"
]

for valid in email_validator(emails):
    print(valid)
