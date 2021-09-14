#with ~ as 굼누 : close()를 사용 안함
#원의 넓이 계산 = pi * 반지름 * 반지름
import math

with open("c:/pyfile/circle_area.txt", 'w')as f:
    radious = 10
    area = math.pi * radious * radious
    f.write("반지름 : %dcm\n" % radious)
    f.write("원의 넓이 : %.2fcm\n" % area)