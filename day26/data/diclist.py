# 학생 5명의 국어, 수학점수 계산
score = [
    {'name': 'A', 'korean': 90, 'math': 70},
    {'name': 'B', 'korean': 85, 'math': 76},
    {'name': 'C', 'korean': 80, 'math': 65},
    {'name': 'D', 'korean': 95, 'math': 85},
    {'name': 'E', 'korean': 85, 'math': 70}
]

# 합계 평균
print('이름 | 총점 | 평균')
for s in score:
    sum_v = s['korean'] + s['math']
    avg = sum_v / 2
    print(s['name'], " | ", sum_v, " | ", avg)

# 과목별 점수 계산
sum_kor = 0
sum_math = 0
n = len(score)
for s in score:
    sum_kor += s['korean']
    sum_math += s['math']
    avg_kor = sum_kor / n
    avg_math = sum_math / n
print()
print("국어 점수의 총점 : %d점" % sum_kor)
print("수학 점수의 총점 : %d점" % sum_math)
print()
print("국어 점수의 평균 : %.1f점" % avg_kor)
print("수학 점수의 평균 : %.1f점" % avg_math)