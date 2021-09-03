#놀이공원 입장료 계산하기
print("♣놀이공원 입장료♣")
x = input("나이를 입력해주세요 : ")
age = int(x)

charge = 0;

if age < 8:
    print("미취학 아동입니다.")
    charge = 1000
elif age >= 8 and age < 14: #elif는 else if 줄인것
    print("초등학생입니다.입니다.")
    charge = 2000
elif age >= 14 and age < 20:
    print("중고등학생입니다.")
    charge = 2500
else:
    print("성인입니다.")
    charge = 3000
print("입장료는 " + str(charge) + "원 입니다.")
print("입장료는 " + format(charge, ',d') + "원 입니다.")
#format(value, "서식문자") - fomat() 천단위 구분기호
# d - 정수형,  s - 문자형
