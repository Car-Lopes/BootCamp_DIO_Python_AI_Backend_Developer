import re

phone = ('(11) 98202-66901')
p1 = re.compile(r'[\W][0-9]{2,2}[\W] [0-9]{5,5}[-][0-9]{4,4}')
check = p1.match(phone)
print(check)