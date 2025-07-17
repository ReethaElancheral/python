
# 4. Create a module `geometry.py` with functions for area and perimeter of circle, square, and triangle.
# 5. Modify the geometry module to include `PI` as a module-level constant.

PI = 3.141592653589793

def area_circle(r):
    return PI * r * r

def perimeter_circle(r):
    return 2 * PI * r

def area_square(a):
    return a * a

def perimeter_square(a):
    return 4 * a

def area_triangle(base, height):
    return 0.5 * base * height

def perimeter_triangle(a, b, c):
    return a + b + c
