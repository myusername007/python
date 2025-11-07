import json
from pathlib import Path

# === 1. Шлях до файлу ===
path = Path("OneDrive/Рабочий стол/Python/tasks.txt")

# === 2. Якщо файл існує — зчитати дані, якщо ні — створити порожній ===
if path.exists():
    with open(path, "r", encoding="utf-8") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
else:
    tasks = []
    path.touch()  # створює порожній файл, якщо його нема

while True:
    print("1.Додати задачу  2.Видалити задачу  3.Показати всі задачі  4.Вихід")
    choice = input("Вибір: ").strip()
    if choice == "4":
        print("До побачення!"); break
    if choice not in ("1", "2", "3"):
        print("Невірний вибір"); continue
    if choice == "1":
       
        x = tasks.append(input("Додаємо задачу: "))
        print("Додано:", tasks[-1])
        
    if choice == "2":
        
        print(tasks)
        y = input("Видалити задачу під номером: ")
        tasks.pop(int(y)-1)
    if choice == "3":
            print(tasks)
            
         # === 4. Після кожної дії — зберегти оновлений список ===
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)