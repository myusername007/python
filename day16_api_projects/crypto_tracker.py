import requests
import json
import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur"

timestamp = datetime.datetime.now().isoformat()
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    if 'bitcoin' not in data:
        raise ValueError("Failed to retrieve cryptocurrency prices.")
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

print(f"\nBitcoin price in USD: {data['bitcoin']['usd']:.2f} $")
print(f"Bitcoin price in EUR: {data['bitcoin']['eur']:.2f} €\n")

with open("btc_price.json", "w+") as f:
    json.dump({'Request time': timestamp, 'result': data}, f, indent=4)