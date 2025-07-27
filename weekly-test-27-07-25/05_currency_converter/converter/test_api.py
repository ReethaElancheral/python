from converter.api import get_supported_currencies

def test_supported_currencies():
    currencies = get_supported_currencies()
    
    if not currencies:
        print("❌ Test Failed: No currencies returned.")
    elif "USD" in currencies and "INR" in currencies:
        print("✅ Test Passed: USD and INR are supported.")
    else:
        print("⚠️ Test Warning: Some common currencies missing.")
        print("Returned currencies:", currencies)


if __name__ == "__main__":
    test_supported_currencies()
