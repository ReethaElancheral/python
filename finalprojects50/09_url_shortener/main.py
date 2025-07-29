# 9. URL Shortener 
# Objective: Convert long URLs to short ones. 
# Requirements: 
#  OOP: URLShortener class. 
#  Dictionary: Map short-code to original URL. 
#  File Handling: Save mappings. 
#  Exception Handling: Invalid URL. 
#  Functions: Shorten, redirect, delete URL. 
#  String Manipulation: Generate random short-code. 
#  Loops: List all shortened URLs. 
#  Generator: Yield expired URLs. 
#  Decorator: @cache for frequent URLs. 

from urlshortener.shortener import URLShortener, InvalidURLException

def main():
    shortener = URLShortener()

    while True:
        print("\n🔗 URL Shortener Menu")
        print("1. Shorten URL")
        print("2. Redirect (Get original URL)")
        print("3. Delete Short URL")
        print("4. List All URLs")
        print("5. Show Expired URLs (older than 7 days)")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            original_url = input("Enter the original URL: ").strip()
            try:
                code = shortener.shorten_url(original_url)
                print(f"✅ Short URL code: {code}")
            except InvalidURLException as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            code = input("Enter short URL code: ").strip()
            url = shortener.redirect(code)
            if url:
                print(f"🔄 Redirecting to: {url}")

        elif choice == "3":
            code = input("Enter short URL code to delete: ").strip()
            shortener.delete_url(code)

        elif choice == "4":
            shortener.list_urls()

        elif choice == "5":
            print("⏳ Expired URLs:")
            expired = list(shortener.expired_urls_generator())
            if not expired:
                print("No expired URLs found.")
            else:
                for code, url in expired:
                    print(f"{code} -> {url}")

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
