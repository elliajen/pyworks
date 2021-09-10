#112p 연습문제
"""
    print("1번")
kor = 80
eng = 75
math = 55
sum = kor + eng + math
avg = sum / 3
print(avg)
print()
"""

print("2번")
n = 13
if n % 2 == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")
print()

print("3번")
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print()

print("4번")
#성별번호가 1이면 남자 아니면 여자
if pin[7] == '1' or pin[7] == '3':
    print("성별번호가 1이므로 남성입니다.")
else:
    print("성별번호가 2이므로 여성입니다.")
"""
print("성별 번호 : " + str(pin[7]))
"""
print()

print("5번")
a = "a:b:c:d"
b = a.replace(':', "#")
print(b)
print()

print("6번")
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
print()

print("7번")
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
