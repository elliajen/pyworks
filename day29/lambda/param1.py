# 매개변수가 1개인 람다 함수
def times(x):   # 3의 배수
    return x * 3

def square(y):  # 제곱수 구하기
    return y * y
result = times(5)
print(result)
print(square(4))

print("lambda")
times2 = lambda x : x * 3
square2 = lambda y : y * y
print("times2(3) = ", times2(3))
print("square(4) = ", square(4))
print("3의 배수 : (lambda x : x * 3)(3) = ", (lambda x : x * 3)(3))
print("제곱수 : (lambda y : y * y)(4) = ", (lambda y : y * y)(4))