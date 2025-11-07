import json
from pathlib import Path

path = Path("OneDrive/Рабочий стол/Python/expenses.txt")

expense = []
if path.exists():

    with open(path, "r",encoding="utf-8" ) as f:
        for line in f:
            try:
                expense = [json.loads(line) for line in f]
            except json.JSONDecodeError:
                expense = []
else:
    path.touch()  # створює порожній файл, якщо його нема

while True:

        print("1.Додати витрату  2.Показати всі витрати  3.Підрахувати загальну суму  4.Очистити файл  5.Вихід")
        choice = input("Вибір: ").strip()
        if choice == "5":
            print("До побачення!"); break

        elif choice not in ("1", "2", "3", "4"):
            print("Неправильний вибір"); continue
        elif choice == "1":
            date = input("Введіть дату витрати: ")
            category = input("Введіть категорію витрати: ")
            amount = input("Введіть суму витрати: ")
            new_expense = [date, category, amount]
            expense.append(new_expense)
            with open (path, "a", encoding="utf-8") as f:
                json.dump(new_expense, f, ensure_ascii=False)
                f.write("\n")
            print("Додано: ", new_expense)
        elif choice == "2":
            with open(path, "r", encoding = "utf-8") as f:
                for line in f:
                    try:
                        expenses = json.loads(line)
                        print(expenses)
                    except:
                        print("FileNotFoundError")

        elif choice == "3":
            total = 0
            with open(path, "r", encoding = "utf-8") as f:
                for line in f:
                    try:
                        expenses = json.loads(line)
                        total += float(expenses[2])
                    except Exception:
                        continue
            print(f"Загальна сума витрат: {total}")
        else:
            expense.clear()
            with open (path, "w", encoding = "utf-8") as f:
                json.dump(expense, f)

                