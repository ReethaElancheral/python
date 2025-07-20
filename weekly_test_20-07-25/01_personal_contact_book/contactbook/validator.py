import re

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
