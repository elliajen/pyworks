#10진수, 2진수, 16진수
#접두사 - 2진수 : 0b, 16진수 : 0x
num = 10
b_num = 0b1010
h_num = 0xA

print("num =", num)
print("b_num = ", b_num)
print("h_num = ", h_num)
print()

#아스키코드
print("코드 33 : ", chr(33))
print("코드 48 : ", chr(48))
print("코드 97 : ", chr(97))
print()

#비트 이동 연산자
#<< - 자리수 커집, >> - 자리수 작아짐
num1 = 5   #이진수 - 00000101
print("num1 << 2 = ", num1 << 2)    #00010100 -> 20
print("num1 >> 2 = ", num1 >> 2)    #00000001 -> 1
print()

#비트 논리연산자
# & | !
num1  = 8  #00001000
num2 = 9   #00001001
print("num1 & num2 = ", num1 & num2)  #& 둘 모두 1일때 1임
print("num1 | num2 = ", num1 | num2)  #| 둘 중 1개 이상이면 1일때 1임
