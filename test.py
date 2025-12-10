import re
text = "Call me at +38 (067) 123-45-67 or 093-555-12-12"
numbers = re.findall(r"\+?[\d ()-]+", text)

for n in numbers:
    n = n.strip()
    clean = re.sub(r"[ ()-]", "", n)
    print(clean)