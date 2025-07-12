# 10. Email Validation Program

# Concepts: string checks, while, functions.
# Ask user to enter valid email.
# Check for @, ., and min length.
# Loop until a valid email is entered.
# Use find(), split(), etc.

def is_valid_email(email):
 
    if len(email) < 6:
        return False
    
  
    if email.count('@') != 1:
        return False
    
    at_index = email.find('@')


    dot_index = email.find('.', at_index)
    if dot_index == -1:
        return False

 
    if ' ' in email:
        return False
    
  
    local_part = email[:at_index]
    domain_part = email[at_index+1:]
    if not local_part or not domain_part:
        return False

    return True


while True:
    email_input = input("Enter a valid email: ").strip()
    if is_valid_email(email_input):
        print("Valid email entered!")
        break
    else:
        print("Invalid email. Please try again.\n")
