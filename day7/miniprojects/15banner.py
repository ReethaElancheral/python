# 15. Banner Generator
# Concepts: string repetition (*), .center()
# Input: title text
# Print a banner:
#  Welcome John

title = input("Enter your banner title: ").strip()


banner_width = max(len(title) + 8, 30)  


border = "*" * banner_width
centered_title = title.center(banner_width)

print("\n" + border)
print(centered_title)
print(border)
