import requests
from bs4 import BeautifulSoup

def scrape(url):
    """
    Generator that yields news headlines one by one from the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to fetch page: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    # This selector depends on the news site structure.
    # Example for BBC News: headlines inside <h3> with class 'gs-c-promo-heading__title'
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

    if not headlines:
        # Fallback: try any <h2> or <h3> tags
        headlines = soup.find_all(["h2", "h3"])

    for headline in headlines:
        text = headline.get_text(strip=True)
        if text:
            yield {"title": text}
