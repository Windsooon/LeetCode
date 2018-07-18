import re

# r = re.findall(r'^(?: +|-|)*[0-9]+', '42')
str = '4193 with words'
str = str.strip()
r = re.findall(r'-?[0-9]+', str)
print(r)
