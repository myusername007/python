import requests

url = "https://open.er-api.com/v6/latest/USD"

try: 
    request = requests.get(url)
    data = request.json()
    if data['result'] != 'success':
        raise ValueError("Failed to retrieve exchange rates.")
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)
print(f"\nLast updated: {data['time_last_update_utc']}")
print(f"Exchange rate from USD to EUR: {data['rates']['EUR']}")
print(f"Exchange rate from USD to PLN: {data['rates']['PLN']}")
print(f"Exchange rate from USD to UAH: {data['rates']['UAH']}\n")