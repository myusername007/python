import requests

url = "https://postman-echo.com/post"

payload = {
    "user": "Roma",
    "task": "learning python",
    "level": "beginner"
}

headers = {
    "Content-Type": "application/json"
}

try: 
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)
print(f"\nSended data: {payload}")
print(f"\nResponse from server: {data['json']}")
print(f"\nHeaders sended: {data['headers']}\n")

