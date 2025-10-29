x = int(input("Введіть ваш вік "))
if x < 13:
    print("Дитина")
elif x < 18:
    print("Підліток")
elif x < 60:
    print("Дорослий")
else:
    print("Пенсіонер")