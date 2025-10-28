print("Введіть перше число")
x = input()
print("Введіть операцію (+,-,*,/)")
i = input()
print("Введіть друге число")
y = input()
if "+" in i:
    z = float(x)+float(y)
    print(f"Результат: {z}")
if "-" in i:
    z = float(x)-float(y)
    print(f"Результат: {z}")
if "*" in i:
    z = float(x)*float(y)
    print(f"Результат: {z}")
if "/" in i:
    z = float(x)/float(y)
    print(f"Результат: {z}")
