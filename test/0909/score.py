li = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
avg = 0.0

for i in li:
 total += i

avg = total / len(li)

print(total)
print("평균 : ", avg)