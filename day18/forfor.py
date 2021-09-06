#중첩 for 문

for i in range(0, 5):   #0~4행
    for j in range(0,5):
        print('가', end = " ")
    print()
        
for i in range(0, 5):   #0~4행
    for j in range(1,6):    #1 ~ 5 열
        num = i * 5 + j
        print(num, end = " ")
    print()
print()

#전체 구구단
for i in range(2, 10):
    print("[", i, "단]")
    for j in range(1, 10):
        #print(i, 'x', j, '=', i*j)
        print("%d x %d = %d" % (i,j,i*j))
    print()
