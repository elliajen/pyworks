#key 반복
#'y' : "계속 반복합니다.", 'n' : "반복을 중단합니다.
#다른 키는 "잘못 입력하셨습니다."

while True:
    answer = input("반복을 계속 할까요? (y/n) ")
    
    if answer == 'y' or answer == 'Y':
        print("계속 반복합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
    
    
