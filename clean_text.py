def clean_text(s):
    ss = s.strip()
    sss = ss.lower()
    ssss = sss.replace(".", " ")
    sssss = ssss.replace(",", " ")
    ssssss = sssss.strip()
    return ssssss

text = str(input("Введіть текст: "))
print("Очищений текст:",clean_text(text),"Кінець.")



