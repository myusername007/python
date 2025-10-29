x = str(input("Введіть текст: "))
i = 0
vowels = "aeєиіїоуюя"
VOWELS = "АЕЄИІЇОУЮЯ"
for y in x:
    if y.lower() in vowels:
        if y.upper() in VOWELS:
            i += 1
print(i)