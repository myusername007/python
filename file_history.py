import json
from pathlib import Path
import datetime

path = Path("history.txt")

while True:
    print(" 1. Додати запис у лог. 2. Показати весь лог.  3. Очистити лог.  4. Вихід.")
    choice = input("Ваш вибір: ")
    if choice == "4":
        print("До побачення!")
        break
    elif choice not in {"1", "2", "3"}:
        print("Невірний вибір, спробуйте ще раз.")
        continue
    elif choice == "1":
        data = input("Введіть ваш запис: ")
        x = datetime.datetime.now()
        date_str = x.strftime("%Y-%m-%d %H:%M:%S")
        with open(path, "a", encoding="utf-8") as f:
            json.dump('[' + date_str + '] '+ "Користувач додав запис: " + "'" + data + "'", f, ensure_ascii=False)
            f.write("\n")
        print("Запис додано до логу.")
    elif choice == "2":
        print("Наявні записи: ")
        if path.exists():
             with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        content = json.loads(line)
                    except json.JSONDecodeError:
                        content = line
                    print(content)
    elif choice == "3":
        if path.exists():
                with open(path, "w", encoding="utf-8") as f:
                    pass
                    print("Лог очищено.")
    
        
        