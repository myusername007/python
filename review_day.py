import json
from pathlib import Path

path = Path("OneDrive/Рабочий стол/Python/notes.txt")
if path.exists():
     with open(path, "r") as f:
        try:
            notes = json.load(f)
        except json.JSONDecodeError:
            notes = []
else:
    notes = []
    path.touch()  # створює порожній файл, якщо його нема

while True:
    print("1.Додати замітку  2.Показати всі замітки  3.Очистити файл  4.Вихід")
    choice = input("Вибір: ").strip()
    if choice == "4":
        print("До побачення!"); break
    elif choice not in ("1", "2", "3"):
        print("Неправильний вибір"); continue
    elif choice == "1":
        notes.append(input("Додати замітку: "))
        print("Додано: ", notes[-1])
        with open (path, "w") as f:
            json.dump(notes,f)
    elif choice == "2":
        print(notes)
    elif choice == "3":
        notes.clear()
        with open(path, "w") as f:
            json.dump(notes, f)
    
