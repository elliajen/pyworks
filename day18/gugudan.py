#구구단 출력
x = input("숫자를 입력해주세요 : ")
dan = int(x)
for i in range(1, 10):
    print(dan, 'x', i, '=', dan*i)
