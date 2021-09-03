#중첩 if

#조건 : 10을 기준으로 큰 수과 작은 수 구분 / 홀짝수 구분
x = input("숫자를 입력해주세요 : ")
n1 = int(x)

'''
if n1 > 10:
    if n1 % 2 ==0:
        print("10보다 큰 짝수 입니다.")
    else:
        print("10보다 큰 홀수 입니다.")
else:
    if n1 % 2 ==0:
        print("10이하의 짝수 입니다.")
    else:
        print("10보다 작은 홀수 입니다.")
        '''

#if ~ elif ~ else
if n1 >10 and n1 % 2 == 0:
    print("10보다 큰 짝수입니다.")
elif n1 > 10 and n1 % 2 ==1:
    print("10보다 큰 홀수입니다.")
elif n1 < 10 and n1 & 2 == 0:
    print("10이하의 짝수입니다.")
else:
    print("10이하의 홀수입니다.")
