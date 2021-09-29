# () - 괄호는 그룹을 구분할 때 사용
# .(점) - 임의의 문자
# findall() - 리스트로 변환
import re

# 태그 괄호 제외
str = "abcd<hr>Thank you"
pat1 = re.compile("<(.*)>")
m1 = re.findall(pat1, str)
print(m1)

# 태그 괄호 포함 찾음
pat2 = re.compile("(<.*>)")
m2 = re.findall(pat2, str)