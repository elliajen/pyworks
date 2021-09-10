import random as r

# lotto (1, 45) - 6개
lotto = []

while len(lotto) < 6:
    rnd = r.randint(1, 45)  # 랜덤 수
    if rnd not in lotto:  # rnd(난수)가 lotto 리스트에 없을떄
        lotto.append(rnd)
"""
for i in range(6):
    rnd = r.randint(1, 45)  #랜덤 수
    if rnd not in lotto:    #rnd(난수)가 lotto 리스트에 없을떄
        lotto.append(rnd)
"""
print(lotto, end=' ')