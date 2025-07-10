# 4. String Formatter Tool

# Concepts: % formatting, replace(), upper(), lower()
# Format: "My name is %s and I earn ₹%.2f" using % formatting
# Modify name using .title() and salary using .replace()

name = input("Enter your name: ").strip()
salary = input("Enter your salary (₹ or commas optional): ").strip()

name = name.title()  
salary_cleaned = salary.replace("₹", "").replace(",", "")  

salary_float = float(salary_cleaned)

output = "My name is %s and I earn ₹%.2f" % (name, salary_float)

print("\nFormatted Output:")
print(output)
