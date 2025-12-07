import requests
from bs4 import BeautifulSoup

url = "https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1"

try: 
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
except Exception as e:
    print("Error:", e)
    exit(1)

rate_tag = soup.find("span", class_="ccOutputRslt")
if not rate_tag:
    print("Не вдалося отримати курс. Сайт змінив структуру.")
    exit(1)

rate = float(rate_tag.text.strip())

inverse_rate = 1 / rate

print(f"USD → EUR: {rate}")
print(f"EUR → USD: {inverse_rate:.5f}")

