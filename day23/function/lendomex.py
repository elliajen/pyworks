import random
import math

# import math
# x = math floor(random.random())
# x   -> 출력

# 0.0 < r < 1.0
print(random.random())

# x <= r <= y - x부터 y 까지의 무작위 수
rend1 = random.randint(1, 6)
rend2 = math.floor(random.random() * 10) + 1
print(rend1)
print(rend2)

# 문자 추출 - random.choice()

fruit = ['포도', '딸기', '사과']
rnd = math.floor(random.random()*len(fruit))
"""
print(rnd)
print(fruit[rnd])
"""
print(random.choice(fruit))