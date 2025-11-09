import requests
import json
from datetime import datetime
from pathlib import Path


path = Path("OneDrive/Рабочий стол/Python/weather_log.txt")

cities = {
    "Kyiv": (50.45, 30.52),
    "Lviv": (49.84, 24.03),
    "Odesa": (46.48, 30.73),
    "Kharkiv": (49.99, 36.23),
    "Dnipro": (48.45, 34.98)
}

def get_weather(city):
    if city not in cities:
        return "❌ Місто не знайдено в базі"

    lat, lon = cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)
    data = response.json()

    temp = data["current_weather"]["temperature"]
    return f"🌤 Температура у {city}: {temp}°C"

# === 3. Виклик ===
city = input("Введіть місто: ").strip()
print(get_weather(city))

current_daytime = datetime.now()
if path.exists():
  with open (path, "a", encoding="utf-8") as f:
                f.write(f"[{current_daytime}] - "); json.dump(get_weather(city), f, ensure_ascii=False)
                f.write("\n")
else:
    path.touch()  # створює порожній файл, якщо його нема