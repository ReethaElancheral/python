from converter.convert import convert_currency
from converter.api import get_supported_currencies
from converter.favorites import add_favorite, remove_favorite, load_favorites
from converter.visualize import show_currency_trend
from converter.utils import format_currency

def main():
    print("🌍 Currency Converter App")
    supported = get_supported_currencies()
    if not supported:
        print("Failed to load supported currencies. Check your internet connection.")
        return

    favorites = load_favorites()

    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. Show Favorites")
        print("3. Add Favorite")
        print("4. Remove Favorite")
        print("5. Show Trend")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            base = input("From Currency (e.g., USD): ").upper()
            target = input("To Currency (e.g., INR): ").upper()
            if base not in supported or target not in supported:
                print("Invalid currency code.")
                continue
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            try:
                result = convert_currency(amount, base, target)
                print(f"{amount} {base} = {format_currency(result)} {target}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            favs = load_favorites()
            print("⭐ Favorite Currencies:", favs if favs else "No favorites yet.")

        elif choice == "3":
            fav = input("Enter currency code to add to favorites: ").upper()
            if fav in supported:
                add_favorite(fav)
                print(f"{fav} added to favorites.")
            else:
                print("Invalid currency code.")

        elif choice == "4":
            fav = input("Enter currency code to remove from favorites: ").upper()
            remove_favorite(fav)
            print(f"{fav} removed from favorites.")

        elif choice == "5":
            base = input("Base Currency: ").upper()
            target = input("Target Currency: ").upper()
            if base not in supported or target not in supported:
                print("Invalid currency code.")
                continue
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            show_currency_trend(base, target, start, end)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
