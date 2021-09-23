# 매개변수가 2개 있는 람다함수
def calc(x, y): # 거듭제곱
    return x ** y
print(calc(2, 3))

print("lambda")
calc2 = lambda x, y: x**y
print("calc2(2,3) = ", calc2(2,3))
print("(lambda x,y : x**y)(2,3) = ", (lambda x, y: x**y)(2, 3))