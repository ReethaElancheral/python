# ✅ 7. Password Strength Tester

# Objective: Validate if password is long enough.
# Requirements:
# Use infinite loop to ask for input.
# If password length < 6, use continue to re-prompt.
# Use break once it meets conditions.
# Use else to print "Password accepted".

while True:
    password = input("Enter a password: ")
    
    if len(password) < 6:
        print("Password too short, try again.")
        continue
    
    break
else:
    print("Password accepted.")  


print("Password accepted.")
