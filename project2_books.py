import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
except Exception as e:
    print("Error: ", e)
    exit(1)

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    stock = book.find("p", class_="instock availability").text.strip()
    link = book.find("a")["href"]
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {stock}")
    print(f"Link: {link}\n")