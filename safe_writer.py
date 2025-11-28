import json
from pathlib import Path

path = Path("data.txt")

text = input("Введіть текст для збереження: ")

if path.exists():
    try: 
        with open(path, "a", encoding="utf-8") as f:
            json.dump(text, f, ensure_ascii=False)
            f.write("\n")
            print("Файл успішно збережено")

    except FileExistsError:
        print("Файл не знайдено")

print("Вміст файлу:")
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        try: 
            content = json.loads(line)
        except json.JSONDecodeError:
            content = line
        print(content)