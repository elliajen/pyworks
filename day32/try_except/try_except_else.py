# try ~ except ~ else
# 오류가 없을때는 try ~ else 가 실행
# 오류가 있을떄는 try ~ except 가 실행
# 항상 작동(오류가 있던 없든 작동)
try:
    print("1번")
    with open('animal2.txt', 'r') as f:
        lines = f.readlines()
except:
    print("2번")

else:
    print("3번")
    for i in lines:
        print(i, end=' ')

finally:
    print("4번")
