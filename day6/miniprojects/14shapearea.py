# 🧩 14. Shape Area Calculator

# Topics Covered: *args, return, lambda
# Requirements:
# Circle, rectangle, square using individual functions
# Use lambda for quick formulas
# Handle invalid inputs using return conditions

import math

circle_area = lambda radius: math.pi * radius ** 2 if radius > 0 else None

def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return None
    return length * width

def square_area(side):
    if side <= 0:
        return None
    return side * side


r = float(input("Enter circle radius: "))
c_area = circle_area(r)
if c_area is not None:
    print(f"Circle Area: {c_area:.2f}")
else:
    print("Invalid radius.")

l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
rec_area = rectangle_area(l, w)
if rec_area is not None:
    print(f"Rectangle Area: {rec_area}")
else:
    print("Invalid rectangle dimensions.")

s = float(input("Enter square side: "))
sq_area = square_area(s)
if sq_area is not None:
    print(f"Square Area: {sq_area}")
else:
    print("Invalid square side.")
