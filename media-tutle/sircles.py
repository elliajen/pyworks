#원 여러개 그리기
import turtle as t
t.shape("turtle")

n = 100
t.speed(0)
t.bgcolor('black')
t.color('purple')
for x in range(n):
    t.circle(100)
    t.left(180/n)

n = 50
t.speed(0)
for x in range(n):
    t.circle(110)
    t.right(30/n)
