import requests

url = "https://restcountries.com/v3.1/name/{country}"


country = input("Enter country name: ")

try:
    request = requests.get(url.format(country=country))
    request.raise_for_status()  # Raise an error for bad status codes
    data = request.json()
    if not data:
        raise ValueError("Failed to retrieve country information.")
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

def get_country_info(data):
    print(f"\nCountry name: {data[0]['name']['common']}")
    print(f"Capital: {data[0]['capital'][0]}")
    print(f"Population: {data[0]['population']}")
    print(f"Area: {data[0]['area']} km²")
    print(f"Currencies: {', '.join(data[0]['currencies'].keys())}")
    print(f"Flag: {data[0]['flags']['png']}\n")


get_country_info(data)