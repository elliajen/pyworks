#threading, datetime 모듈 임포트

# 일정시간이 지나면 종료되는  threading 모듈 사용
import threading
import datetime

def call():
    print("타이머 종료!!")
    print(datetime.datetime.now())       # call 호출 후 시간 출력

# 현재시간
print(datetime.datetime.now())

# 10초 후에 종료
timer = threading.Timer(5, call)
timer.start()

