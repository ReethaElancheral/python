# ✅ 20. OTP Retry System

# Objective: Simulate OTP entry with retry option.
# Requirements:
# OTP is fixed.
# Use while loop to allow 3 retries.
# Use break if entered OTP is correct.
# Use else to print "OTP failed".

correct_otp = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_otp = input("Enter OTP: ").strip()
    if entered_otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")
        attempts += 1
else:
    print("OTP failed. Maximum attempts reached.")
