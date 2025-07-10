# 19. OTP Generator (One-Time Password)

# Concepts: slicing, indexing, repetition
# Input: mobile number
# Output: OTP like "78A5Z1" made using last 4 digits + random letters (simulate)

import random
import string


mobile = input("Enter your 10-digit mobile number: ").strip()

if len(mobile) == 10 and mobile.isdigit():
 
    last_four = mobile[-4:]

    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))

    otp = last_four[:2] + random_chars + last_four[2:]

    print("Generated OTP:", otp)
else:
    print("❌ Please enter a valid 10-digit mobile number.")
