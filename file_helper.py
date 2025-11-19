import os
import shutil

while True:
    print ("1.Показати файли  2.Показати файли з розміром  3.Створити backup/  4.Скопіювати файл в backup/  5.Вихід")
    сhoice = input("Вибір: ").strip()
    if сhoice == "5":
        print("До побачення!"); break
    elif сhoice not in ("1","2","3","4"):
        print("Неправильний вибір"); continue
    elif сhoice == "1":
        files = os.listdir()
        for file in files:
            print(file)
    elif сhoice == "2":
        files = os.listdir()
        for file in files:
            size = os.path.getsize(file)
            print(f"{file}: {size} bytes")
    elif сhoice == "3":
        os.makedirs("backup", exist_ok=True)
        print("Папку backup/ створено")
    elif сhoice == "4":
        file_name = input("Введіть назву файлу для копіювання: ").strip()
        if os.path.exists(file_name):
            try: 
                shutil.copy(file_name, "backup/")
                print(f"Файл {file_name} скопійовано в backup/")
            except Exception as e:
                print(f"Помилка копіювання файлу: {e}")

