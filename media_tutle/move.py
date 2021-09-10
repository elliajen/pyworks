import turtle as t

t.shape("turtle")

#사각형
"""
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
"""
n = 4
d = 150
t.pensize(2)
for i in range(n):
    t.forward(d)
    t.right(360/n)

#삼각형
n = 3
t.color("green")
for i in range(3):
    t.forward(d)
    t.left(360/n)

#원
t.pensize(3)
t.color("blue")
t.circle(50)    #반지름이 50px

