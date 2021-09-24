# *와 +차이점
import re
# '*'은 문자 0번 이상 반복
# '+'는 문자 1번이상 반복
p=re.compile("ca*t")
m1 = re.findall(p, "caat")
print(m1)

m2=re.findall(p, "ct")
print(m2)

p2 = re.compile("ca+t")
m1 = re.findall(p2, "caat")
print(m1)

m2=re.findall(p2, "ct")
print(m2)