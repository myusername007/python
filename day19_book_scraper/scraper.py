import json
from bs4 import BeautifulSoup
import re
import requests
from pathlib import Path

path = Path("/Users/root7/myproject/day19_book_scraper/data.json")
url = "https://books.toscrape.com/"

try: 
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
except Exception as e:
    print("Error: ", e)
    exit(1)

def get_books():
    books_data = [] 
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title_tag = book.find("h3").find("a")
        title = title_tag["title"] if title_tag else "N/A"
        
        price_str = book.find("p", class_="price_color").text
        price = re.findall(r"[\d\.]+", price_str)[0]
        if not price: price = "N/A"
        
        stock = book.find("p", class_="instock availability").text.strip()
        clean_stock = re.sub(r"\s+", " ", stock)
        if not clean_stock: clean_stock = "N/A"
        
        link = book.find("a")["href"]
        if not link: link = "N/A"
        
        rating_class = book.find("p", class_="star-rating")["class"]
        rating = rating_class[1]
        if not rating: rating = "N/A"
        
        
        book_info = {
            "title": title,
            "price": f"{price}£",
            "stock": clean_stock,
            "link": f"https://books.toscrape.com/{link}",
            "rating": f"{rating.lower()} out of five"
        }
        
        books_data.append(book_info)
        
        
        print(f"Title: {title}")
        print(f"Price: {price}£")
        print(clean_stock)
        print(f"Link: https://books.toscrape.com/{link}")
        print(f"Rating: {rating.lower()} out of five\n")
    
    return books_data  


books_list = get_books()


with open(path, "w", encoding="utf-8") as f:
    json.dump(books_list, f, ensure_ascii=False, indent=4)

print(f"Дані збережено у {path}\n")
