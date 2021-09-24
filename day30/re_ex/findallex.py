# findall()함수
import re
str = "Two is too"
m1 = re.findall("T[ow]o",str)
print(m1)

m2 = re.findall("T[ow]o",str, re.IGNORECASE)    # 대소문자 허용
print(m2)

pat = re.compile("T[^o]o")
m3 = re.findall(pat, str)
print(m3)