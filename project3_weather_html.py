import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/ukraine/kyiv"

try:
    response = requests.get(url)
    response.raise_for_status
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
except Exception as e:
    print("Error: ", e)
    exit(1)

temp = soup.find("div", id="qlook").find("div", class_="h2").text
disc = soup.find("div", id="qlook").find("p").contents[0]
print(f"Current temperature: {temp}")
print(f"{disc}")
print(f"Feels like: {temp}")