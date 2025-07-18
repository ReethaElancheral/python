from decimal import Decimal
import math

def power(a, b):
    return Decimal(a) ** Decimal(b)

def sqrt(a):
    a = Decimal(a)
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return Decimal(math.sqrt(a))
