x = ["apple", "cherry", "mango"]
y = ["apple", "cherry", "mango","banana"]
set1 = set(x)
set2 = set(y)
numb = 0
print("Спільні елементи множин:")
for i in set1 & set2:
    print(i)
    numb +=1
print("Кількість спільних елементів:", numb)
   