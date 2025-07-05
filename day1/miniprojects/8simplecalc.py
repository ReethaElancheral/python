## 8. Simple Calculator

# - Prompt the user for two numbers and an operation (add, subtract, multiply, divide).
# - Perform the calculation and print the result.
# - Show types of all inputs and the result.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")


add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 

results = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}



result = results[operation]

print("Result:", result)
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))
print("Type of result:", type(result))



