#179p 1번
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(10))
print(is_odd(11))

#179p 2번
def avg_number(*args):
    result = 0      #합계
    for i in args:
        result += i
    return result / len(args)

print(avg_number(1, 2))
print(avg_number(1, 2, 3, 4, 5))

"""
#179p 3번
x = input("첫번째 숫자를 입력하세요: ")
input1 = int(x)
y = input("두번째 숫자를 입력하세요: ")
input2 = int(y)

total = input1 + input2
print("두 수의 합은 %s입니다." % total)
"""

#179p 4번
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#179p 5번
f1 = open("test_5.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test_5.txt", 'r')
print(f2.read())
f2.close()
"""
#179p 6번
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test_6.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()
"""
#179p 7번
f = open('test_7.txt', 'r')
body = f.read()
f.close()

body =body.replace('java', 'pyrhon')

f = open('test_7.txt', 'w')
f.write(body)
f.close
