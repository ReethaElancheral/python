# main.py


# 20. Currency Converter (API-Based) 
# Objective: Convert between currencies using real-time rates. 
# Requirements: 
#  OOP: CurrencyConverter class. 
#  API Call: Use requests to fetch exchange rates. 
#  Exception Handling: API errors, invalid currencies. 
#  Dictionary: Store conversion rates. 
#  Functions: Convert, list supported currencies. 
#  Loops: Allow multiple conversions. 
#  Generator: Yield historical rates (mock data). 
#  Decorator: @cache_rates to avoid repeated API calls.


from converter.core import CurrencyConverter

def main():
    print("💱 Welcome to Currency Converter CLI")
    converter = CurrencyConverter()

    while True:
        print("\nMenu:\n1. Convert Currency\n2. List Supported Currencies\n3. View Historical Rates\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                from_curr = input("From Currency (e.g., USD): ").upper()
                to_curr = input("To Currency (e.g., INR): ").upper()

                result = converter.convert(amount, from_curr, to_curr)
                if result is not None:
                    print(f"{amount} {from_curr} = {result} {to_curr}")
            except ValueError:
                print("Invalid input. Please enter numeric value.")

        elif choice == '2':
            print("Supported Currencies:")
            print(", ".join(converter.list_currencies()))

        elif choice == '3':
            print("📅 Mock Historical Rates:")
            for rate in converter.historical_rates():
                print(rate)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
