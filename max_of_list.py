user_list = list(input("Введіть список чисел: "))
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max else max

print("Найбільше число:", find_max(user_list))