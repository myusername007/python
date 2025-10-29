import random

x = random.randint(1,10)
y = 0
while x != y:
    y = int(input("Вгадай загадане число (1-10): "))
    if x != y:   
        print("Не вгадав! :)")
else:
    print("Вгадав :(")