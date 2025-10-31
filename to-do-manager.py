tasks = []

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
            