import requests
from bs4 import BeautifulSoup

url = "https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1"

try: 
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
except Exception as e:
    print("Error: ",e)
    exit(1)

usd = soup.find("span", class_="ccOutputTxt")
euro = soup.find("span", class_="ccOutputRslt")
print(f"From USD to EUR: {usd.text} {euro.text}")
