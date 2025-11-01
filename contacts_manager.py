cont1 = ("Ivan", 380992432304)
cont2 = ("Vova", 380664256407)
cont3 = ("Eugen", 380954325678)
contacts = [cont1, cont2, cont3]   # можна коротше

while True:
    print("1.Додати контакт  2.Знайти контакт  3.Вивести контакти  4.Вихід")
    choice = input("Вибір: ").strip()
    
    if choice == "4":
        print("До побачення!")
        break
    
    elif choice not in ("1", "2", "3"):
        print("Невірний вибір")
        continue
    
    elif choice == "1":
        x = input("Ім'я контакту: ")
        y = int(input("Номер: "))
        contacts.append((x, y))
        print("Контакт додано")
    
    elif choice == "2":
        name = input("Введіть ім'я контакту: ")
                            
        for x, y in contacts:
            if x == name:
                print("Знайдено:", x,":", y)
                break;
            else:
                print("Не знайдено!")
    
    elif choice == "3":
        print("Список контактів:")
        for x, y in contacts:
            print(x,":", y)

