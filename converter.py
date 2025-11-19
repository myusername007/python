import requests



base = "USD"
url = f"https://open.er-api.com/v6/latest/{base}"
try:
    response = requests.get(url)
    response.raise_for_status() 
except:
    print("Request error")

data = response.json()
if data["result"] != "success":
    print("API error")
    exit()
    
rates = data["rates"]
print("Convert from:", base)

amount = float(input("Enter amount: "))
target = input("Convert to (currency code): ").strip().upper()

if target in rates:
    result = amount * rates[target]
    print(f"{amount} {base} = {result:.2f} {target}")
else:
    print("Currency not found") 