#문자열 함수
print("split()함수 - 구분자(구분기호 - 공백 , :)")
s1 = "banana grape peach"
s1 = s1.split(' ')  #공백문자로 구분되어 리스트 형태로 반환
print(s1)
print(s1[0])

print()

print("replace()함수 - 문자 체인지")
s2 = "Hello, World"
print(s2)
s2 = s2.replace("World", "Korea")
print(s2)

print()

print("format() 함수 - 지정된 숫자에 맞게 해당 항목이 들어감")
s3 = 'My name in {0}. I am {1} years old. I like {2}'.format('Ellia', 22, 'Art')
print(s3)

print("I eat {0} apples".format(3))
n=3
print("I eat {0} apples".format(n))
n=5
print("I eat {0} apples. So I was sick for {1} days".format(n, day))
