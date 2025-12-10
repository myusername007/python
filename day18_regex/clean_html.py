import re

text = "<div><h1>Hello</h1><p>This is <b>bold</b> text</p></div>"

data =  re.sub("<[^>]+>","",text)
print(data)
