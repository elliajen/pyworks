import threading
# threading.Timer : 일정 주기마다 함수를 실행하는 클래스
# threading.Timer(시간,함수)
def repeat():
    print("2초 간격으로 반복 실행")
    timer = threading.Timer(2, repeat)  # callback 함수
    timer.start()

repeat()