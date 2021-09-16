# 학생 5명의 국어, 수학점수 계산
score = [
    {'name': '이연희', 'korean': 90, 'math': 70, 'science': 65},
    {'name': '천서연', 'korean': 85, 'math': 76, 'science': 75},
    {'name': '이소라', 'korean': 80, 'math': 65, 'science': 85},
    {'name': '오혜리', 'korean': 95, 'math': 85, 'science': 55},
    {'name': '오서리', 'korean': 85, 'math': 70, 'science': 35}
]

# 합계 평균
print('이름 | 총점 | 평균')
for s in score:
    sum_v = s['korean'] + s['math']+ s['science']
    avg = sum_v / 3
    print("%s %d %.1f" % (s['name'], sum_v, avg), "점")

# 과목별 점수 계산
sum_kor = 0
sum_math = 0
sum_science = 0
n = len(score)
for s in score:
    sum_kor += s['korean']
    sum_math += s['math']
    sum_science += s['science']
    avg_kor = sum_kor / n
    avg_math = sum_math / n
    avg_science = sum_science / n
print()
print("국어 점수의 총점 : %d점" % sum_kor)
print("수학 점수의 총점 : %d점" % sum_math)
print("과학 점수의 총점 : %d점" % sum_science)
print()
print("국어 점수의 평균 : %.1f점" % avg_kor)
print("수학 점수의 평균 : %.1f점" % avg_math)
print("과학 점수의 평균 : %.1f점" % avg_science)