import requests

url = "https://api.chucknorris.io/jokes/random"

def get_joke():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'value' not in data:
            raise ValueError("Failed to retrieve joke.")
        return data['value']
    except Exception as e:
        return f"An error occurred: {e}"
    
print(f"\n🤣 Жарт дня: {get_joke()}\n")
    
    