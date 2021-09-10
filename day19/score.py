#학생의 시험점수 합격 판단
#시험  점수가 60점 이상이면 '합격', 아니면 '불합격'
score = [90,45,67,59,85]
idx = 0
for i in score:
    idx += 1
    if i >= 60:
       print(str(idx) + "번 학생은 " + str(i) + "점으로 합격입니다.")
       print()
    else:
        print(str(idx) + "번 학생은 " + str(i) + "점으로 불합격입니다.")
        print()
print()

print("for ~ in range() 반복문")
n = len(score)
for i in range(0, n):
    if score[i] >= 60:
        print(str(i+1) + "번 학생은 합격입니다.")
    else:
        print(str(i+1) + "번 학생은 불합격입니다.")

#성적의 합계, 평균
total = 0
avg = 0.0

for i in score:
    total += i
    avg = total / len(score)

print("합계 : " + str(total))
print("평균 : " + str(avg))
