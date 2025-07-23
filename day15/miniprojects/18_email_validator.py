# 18. Email Validator

# Use Case: Validate list of emails from input. 
# Exception Handling Goals:
# Raise InvalidEmailFormatError
# Log all invalid emails
# Use try-except inside a list loop

import re
import logging

# Setup logging
logging.basicConfig(filename="invalid_emails.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

# Custom Exception
class InvalidEmailFormatError(Exception):
    pass

def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailFormatError(f"Invalid email format: {email}")

def email_validator():
    emails_input = input("Enter emails separated by commas: ")
    emails = [email.strip() for email in emails_input.split(',')]

    valid_emails = []
    for email in emails:
        try:
            validate_email(email)
        except InvalidEmailFormatError as iee:
            logging.error(iee)
            print(f"❌ {iee}")
        else:
            valid_emails.append(email)

    print(f"\n✅ Valid emails ({len(valid_emails)}):")
    for v in valid_emails:
        print(f"  {v}")

if __name__ == "__main__":
    email_validator()
