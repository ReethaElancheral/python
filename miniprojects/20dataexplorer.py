## 20. Data Type Explorer

# - Ask the user to enter any value.
# - Print the value and its data type using type().
# - Ask the user to specify if it should be converted (int, float, bool, str), convert, and display the result and new type.

value = input("Enter any value: ")

print(f"Value entered: {value}")
print(f"Type before conversion: {type(value)}")

convert_to = input("Enter the type to convert to (int, float, bool, str): ").strip().lower()

if convert_to == "int":
    converted_value = int(value)
elif convert_to == "float":
    converted_value = float(value)
elif convert_to == "bool":

    converted_value = bool(value)
elif convert_to == "str":
    converted_value = str(value)
else:
    converted_value = value 

print(f"Converted value: {converted_value}")
print(f"Type after conversion: {type(converted_value)}")
