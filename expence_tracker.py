import json
from pathlib import Path

path = Path("OneDrive/Рабочий стол/Python/expenses.txt")
if path.exists():
     with open(path, "r",encoding="utf-8" ) as f:
        for line in f:
            try:
                expense = json.load(f)
            except json.JSONDecodeError:
                expense = []
else:
    expense = []
    path.touch()  # створює порожній файл, якщо його нема

    while True:
        print("1.Додати витрату  2.Показати всі витрати  3.Підрахувати загальну суму  4.Очистити файл  5.Вихід")
        choice = input("Вибір: ").strip()
        if choice == "5":
            print("До побачення!"); break

        elif choice not in ("1", "2", "3", "4"):
            print("Неправильний вибір"); continue
        elif choice == "1":
            expense.append(input("Введіть дату витрати: "))
            expense.append(input("Введіть категорію витрати: "))
            expense.append(input("Введіть суму витрати: "))
            print(expense)
            with open (path, "a", encoding="utf-8") as f:
                json.dump(expense, f, ensure_ascii=False)
                f.write("\n")
        elif choice == "2":
            with open(path, "r", encoding = "utf-8") as f:
                for line in f:
                    try:
                        expenses = json.loads(line)
                        print(expenses)
                    except:
                        print("FileNotFoundError")

        elif choice == "3":
             with open(path, "r", encoding = "utf-8") as f:
                for line in f:
                    try:
                        expenses = json.loads(line)
                        print(expenses[2])
                    except:
                        print("FileNotFoundError")

        elif choice == "4":
            expense.clear()
            with open (path, "w", encoding = "utf-8") as f:
                json.dump(expense, f)