# 매개변수가 없는 lambda
# 안녕을 10번 반복 -> 콜백함수(매개변수가 함수인것)
def call_10(func):
    for i in range(10):
        func()

def say_hello():
    print("안녕")

say_hello()
call_10(say_hello)

print("lambda")
talk = lambda : print("안녕하세요")
talk()
call_10(talk)
call_10(lambda : print("잘가"))