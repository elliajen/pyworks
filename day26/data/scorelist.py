# 학생 5명의 국어와 수학점수 계산
score = [[90, 70],
         [85, 76],
         [80, 65],
         [95, 85],
         [85, 70]
         ]

# 합계와 평균
sum_kor = 0
sum_math = 0
n = len(score)

for i in range(0, n):
    sum_kor += score[i][0]
    sum_math += score[i][1]

avg_kor = sum_kor / n
avg_math = sum_math / n

print("국어 합계 = %d점" % sum_kor)
print("수학 합계 = %d점" % sum_math)
print("국어 평균 = %.1f점" % avg_kor)
print("수학 평균 = %.1f점" % avg_math)