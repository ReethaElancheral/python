# 6. Resume Title Generator

# Concepts: .join(), .upper(), f-strings
# Input: first name, last name, role
# Output: "JOHN | SMITH | PYTHON DEVELOPER" using .join() and .upper()


first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
role = input("Enter your desired role: ").strip()

first_name = first_name.upper()
last_name = last_name.upper()
role = role.upper()

resume_title = " | ".join([first_name, last_name, role])

print("\nGenerated Resume Title:")
print(resume_title)
