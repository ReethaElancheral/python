## 5. Temperature Converter

# - Ask the user to enter temperature in Celsius.
# - Convert it to Fahrenheit and print the result with an f-string.
# - Display the type before and after conversion.


celsius = input("Enter temperature in Celsius: ")
print("Type before conversion:", type(celsius))

celsius = float(celsius)
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F.")
print("Type after conversion:", type(celsius))
