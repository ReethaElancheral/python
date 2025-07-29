# 27. Web Scraper (News Headlines) 
# Objective: Scrape headlines from a news site. 
# Requirements: 
#  Modules: requests, BeautifulSoup. 
#  Dictionary: Store headlines ({"title": "..."}). 
#  Exception Handling: HTTP errors. 
#  Functions: scrape(url). 
#  Loops: Extract multiple headlines. 
#  Generator: Yield headlines one by one. 

from scraper.core import scrape

def main():
    print("📰 News Headlines Scraper")
    url = input("Enter news site URL: ").strip()

    try:
        print("\nHeadlines found:\n")
        for idx, headline in enumerate(scrape(url), start=1):
            print(f"{idx}. {headline['title']}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
