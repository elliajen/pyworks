#튜플(tuple) - 변경 삭제 할 수 없다.
t = ('코스모스', '민들레', '국화')
print(t)
print(t[:2])
print(t[1:])
#del t[0] - 삭제 안됨
#t[2] = "매화" - 변경안됨

t2 = (1,2,3)
t3 = (4,)   #1개 추가하기(쉼표를 붙임)
print(t2)
print(t3)
print(t2+t3)
