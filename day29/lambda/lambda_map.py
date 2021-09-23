# map(함수, 리스트), filter() 함수와 같이 사용하기
# list([리스트]) -> 리스트로 반환(출력)
def time(a):
    a2 = [] # 3의 배수를 저장할 빈 리스트
    for i in a:
        a2.append(i * 3)
    return a2

v = [1, 2, 3, 4]
print(time(v))


# 람다함수
times = lambda x : x * 3
print(list(map(times, v)))