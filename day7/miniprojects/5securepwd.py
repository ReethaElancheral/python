# 5. Secure Password Masker

# Concepts: indexing, string multiplication, slicing
# Input a password like "MySecret123"
# Output: "M*******3" (first and last char shown, rest masked using *)
# Use slicing and repetition (* operator)

password = input("Enter your password: ").strip()

if len(password) < 3:
    print("Password too short to mask.")
else:
    masked = password[0] + "*" * (len(password) - 2) + password[-1]

    print("Masked Password:", masked)
