## 10. Currency Converter

# - Ask the user for an amount in USD.
# - Convert it to INR (use a fixed rate, e.g., 1 USD = 83 INR).
# - Print the result using an f-string.
# - Show the type after conversion.

usd_amount = float(input("Enter amount in USD: "))

conversion_rate = 85.63

inr_amount = usd_amount * conversion_rate


print(f"{usd_amount} USD is equal to {inr_amount} INR.")
print("Type of INR amount:", type(inr_amount))

