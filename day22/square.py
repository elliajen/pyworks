# 제곱수 계산하는 함수 정의
def square(x):
    return x * x

# 거듭제곱을 계산하는 함수

def double_times(x, y):
    return x ** y

# 절대값 구하는 함수
def abs_v(x):
    if x < 0:
        return -x
    else:
        return x

"""
# 절대값 구하는 함수2
def abs_v2(x):
    y = x * x
    return math.aqrt(y)
"""

# 호출
n = square(5)
n2 = double_times(2, 3)

# 출력
print("제곱수 : ", n)
print("거듭제곱수 : ", n2)
print("절대값 : ", abs_v(-10))