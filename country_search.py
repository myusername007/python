import requests
import json
from pathlib import Path

path = Path('OneDrive/Рабочий стол/Python/countries_log.txt')

def get_country(country):
    if country is False:
        print("Country error")

    url = f"https://restcountries.com/v3.1/name/{country}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except:
        print("Request error")

    data = response.json()

    c_name = data[0]['name']['official']
    c_capital = data[0]['capital'][0]
    c_population = data[0]["population"]
    c_area = data[0]["area"]
    first_currency_key = next(iter(data[0]["currencies"]))
    c_currency = data[0]["currencies"][first_currency_key]['name']

    c_data = [c_name,c_capital,c_population,c_area,c_currency]
    return f"Country: {c_name}\nCapital: {c_capital}\nPopulation: {c_population}\nArea: {c_area}\nCurrency: {c_currency}"

country = input("Введіть назву країни: ").strip()
print(get_country(country))

if path.exists():
  with open (path, "a", encoding="utf-8") as f:
                json.dump(get_country(country), f, ensure_ascii=False)
                f.write("\n")
else:
    path.touch()  # створює порожній файл, якщо його нема
