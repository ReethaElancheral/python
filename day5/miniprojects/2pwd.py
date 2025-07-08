# ✅ 2. Password Checker with Limited Attempts

# Objective: Check password input with a maximum of 3 tries.
# Requirements:
# Use while loop with attempts counter.
# Use break to exit if password is correct.
# After the loop, use else to say “Too many attempts!” if not successful.

correct_password = "pass123"
attempts = 0

while attempts < 3:
    entered_password = input("Enter your password: ")
    
    if entered_password == correct_password:
        print("Access Granted ✅")
        break  
    
    print("Incorrect password ❌")
    attempts += 1

else:
    print("Too many attempts! Access Denied 🚫")
