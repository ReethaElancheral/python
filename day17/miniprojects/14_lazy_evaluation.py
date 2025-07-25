# 14. Lazy Evaluation of Complex Calculations 
# Objective: Generate results of math operations only when needed. 
# Requirements: 
#  Input: list of (a, b, op) tuples. 
#  Generator yields result only when next() is called. 
#  Use generator expression for +, -, *, /.

def lazy_math_evaluator(tasks):
    for a, b, op in tasks:
        if op == '+':
            yield a + b
        elif op == '-':
            yield a - b
        elif op == '*':
            yield a * b
        elif op == '/':
            yield a / b if b != 0 else 'Division by zero'

# Example usage:
operations = [(5, 3, '+'), (10, 2, '-'), (4, 6, '*'), (8, 0, '/')]
evaluator = lazy_math_evaluator(operations)

print("Lazy Math Results:")
for result in evaluator:
    print(result)
