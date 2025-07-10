# 16. Slug Generator for Blog Titles

# Concepts: .lower(), .replace(), .strip()
# Input: " Python   Basics for Beginners "
# Output: "python-basics-for-beginners"


title = input("Enter blog title: ")


slug = title.strip()            
slug = slug.lower()            
slug = " ".join(slug.split())  
slug = slug.replace(" ", "-")   

print("Generated Slug:", slug)
