#숫자를 입력받아 그 수까지 반복하는 프로그램
x = input("몇번 반복할까요? ")
n = int(x)

i = 0
sum = 0
while i < n:
    i += 1
    sum += i
    print(i)

print()
print(str(n) + "회 반복했습니다.")
print("반복한 수의 합계는 " + str(sum) + "입니다.")
