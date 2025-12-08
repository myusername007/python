import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
except Exception as e:
    print("Error: ", e)
    exit(1)

quotes = soup.find_all("div", class_="quote")
for quote in quotes: 
    if len(quotes)<=10:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [t.text for t in quote.find_all("a", class_="tag")]

        print(f"\n'{text}' - {author}")
        print(f"Tags: {tags}")