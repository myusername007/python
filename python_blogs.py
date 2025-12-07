import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/"

try:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
except Exception as e:
    print(f"Error: {e}")
    exit(1)
    
posts = soup.select("ul.list-recent-posts li") 

for p in posts:
    title = p.find("a").text.strip()
    link = p.find("a").get("href")
    date = p.find("time").text.strip()

    print(f"📌 Назва: {title}")
    print(f"🔗 URL: {link}")
    print(f"📅 Дата: {date}")
    print("-" * 40)
   
