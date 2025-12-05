import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true"

try: 
    request = requests.get(url)
    request.raise_for_status()  # Raise an error for bad status codes
    data = request.json()
    if 'current_weather' not in data:
        raise ValueError("Failed to retrieve weather information.")
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

print(f"\nCurrent temperature in Kyiv: {data['current_weather']['temperature']}°C")
print(f"Wind speed: {data['current_weather']['windspeed']} km/h")
print(f"Weather code: {data['current_weather']['weathercode']}\n")

