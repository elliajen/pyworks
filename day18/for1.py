#for 문 사용
#range(시작값 ,종료값  +1, [증감 (생략 가능)])
#1은 기본이므로 생략 가능
"""
for i in range(1, 6):
    print(i)    #range 범위
    
"""

#0 ~ 9 출력 : 초기값이 없는 경우 0부터 시작임
#옆으로 정렬 print(--, end = " (공백 spacebar)")
for i in range(10):
    print(i, end =" ")

print()

# 1 ~ 10 중 홀수 출력
for n in range(1, 11, 2):
    print(n, end=" ")

print()

# 1 ~ 10 중 홀수 출력
for x in range(1, 11, 1):
    if x % 2 == 1:
        print(x, end=" ")
