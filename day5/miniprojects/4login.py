# ✅ 4. Simple Login System

# Objective: Allow login until correct password is entered.
# Requirements:
# Use while True for infinite loop.
# Ask user for password input.
# Break if correct password entered.
# Use pass as placeholder for future logging.

correct_password = "pass123"

while True:
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Login Successful ✅")
        
        pass  
        break  
    
    print("Incorrect password. Try again ❌")
