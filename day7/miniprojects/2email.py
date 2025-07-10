# 🧩 2. Email Template Customizer

# Concepts: .format(), .replace(), string slicing, f-strings
# Input: name, course, duration
# Template: "Dear {name}, your {course} course starts in {duration} days."
# Replace placeholders using .format() or f-string

# Email Template Customizer using .format()

name = input("Enter Your Name: ").strip()
course = input("Enter Your course: ").strip()
duration = input("Enter Duration of the course in days: ").strip()

template = "Dear {name}, your {course} course starts in {duration} days."

custom_email = template.format(name=name, course=course, duration=duration)

print("\nCustomized Email:")
print(custom_email)

# Email Template Customizer using f-string

name = input("Enter your name: ").strip()
course = input("Enter your course: ").strip()
duration = input("Enter course duration in days: ").strip()

email = f"Dear {name}, your {course} course starts in {duration} days."

print("\nCustomized Email:")
print(email)


#  Email Template Customizer using .replace()

template = "Dear NAME, your COURSE course starts in DURATION days."

name = input("Enter your name: ").strip()
course = input("Enter your course: ").strip()
duration = input("Enter course duration in days: ").strip()

email = template.replace("NAME", name).replace("COURSE", course).replace("DURATION", duration)

print("\nCustomized Email:")
print(email)
