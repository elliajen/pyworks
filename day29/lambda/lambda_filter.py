# filter(함수, 리스트) 를 lambda()와 함께 이용 -> 필터링
def negative2(v):
    v2 = []
    for i in v:
        if i < 0:
            v2.append(i)
    return v2

v = [-5, 1, 2, -11, 7]

print(negative2(v))

negative = lambda x : x < 0 # 음수를 계산하는 함수

print(list(filter(negative, v)))
