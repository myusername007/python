import re

text = "Roma bought items for 12, then 7, then 45, total?"

s = 0
for number in re.findall("\d+", text):
    s += int(number)

print(s)