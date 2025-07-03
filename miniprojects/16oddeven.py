## 16. Odd/Even Number Identifier

# - Ask the user for a number.
# - Print whether it’s odd or even.
# - Print the type of the number before and after conversion.

num_str = input("Enter a number: ")
print("Type before conversion:", type(num_str))

num = int(num_str)
print("Type after conversion:", type(num))

result = {
    True: f"{num} is even.",
    False: f"{num} is odd."
}

print(result[num % 2 == 0])
