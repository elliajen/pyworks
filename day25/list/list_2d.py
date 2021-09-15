d2 = [  # 컴마로 구분
    [10, 20],
    [30, 40],
    [50, 60]
]
print("리스트의 크기(행) : ", len(d2))
print("리스트의 크기( 열) : ", len(d2[0]))
print("리스트의 크기( 열) : ", len(d2[1]))

print()

# 전체요소 출력
for i in range(len(d2)):
    for j in range(len(d2[i])):
        print(d2[i][j], end = ' ')
    print()

print()

#합계와 평균
sum_v = 0
count = 0   # 2차원일떄는 개수가 필요
for i in range(len(d2)):
    for j in range(len(d2[i])):
        sum_v += d2[i][j]
        count += 1      # 1번 반복할때마다 1증가
        print("sum_v = " , sum_v, "|| d2[i][j] = ", d2[i][j], "||", count, "번째")
avg = sum_v / count
print("합계 : %d" % sum_v)
print("개수 : %d" % count)
print("평균 : %.1f" % avg)
