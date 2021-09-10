#주사위 10번 던지기

import random

for x in range(1,11):
    dice = random.randint(1, 6)
    print(dice, end = ' ')
print()
print("=================")

"""
주사위 두개를 10번 던지기
두 눈의 합이 7이면 "Seven Thrown!"
두 눈의 합이 11이면 "Eleven Thrown!"
두 눈의 수가 같으면 "Doble Thrown!"
"""
for x in range(1, 11):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print(total)
    if total == 7:
        print("Seven Thrown!")
    elif total == 11:
        print("Eleven Thrown!")
    elif d1 == d2:
        print("Doble Thrown!")
