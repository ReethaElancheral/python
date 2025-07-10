# 🧩 1. Personal Bio Generator

# Concepts: f-strings, +, .upper(), .strip(), len()
# Ask the user for name, age, job title
# Clean extra spaces using .strip()
# Capitalize name using .upper()
# Display: "Hi, I'm JOHN. I'm 30 years old and I work as a Developer"
# Count total characters in the bio using len()

name = input("Enter your Name: ").strip().upper()
age = input("Enter your Age: ").strip()
job_title = input("Enter your Job title: ").strip()

bio = (f"Hi I'm {name}. I'm {age} years old and I work as a {job_title}")
print(f"Personal Bio:")
print(bio)
print(f"Total characters in Bio is", len(bio))



