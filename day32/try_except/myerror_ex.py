# 예외만들기 - 사용자가 직접 만들기
# Exception 클래스를 상속하여 만든다.
class MyError(Exception):
    #pass
    def __str__(self):  # 문자로 리턴해줌
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError() # Error 를 발생시킴(미뤄놓음)
    print(nick)
# Error 를 사용하는 곳에서 try ~ except 처리해야 함
try:
    say_nick('Hero')
    say_nick('Angel')
    say_nick('바보')
except MyError as e:        # e : Exception
    # print('허용되지 않는 별명입니다.')
    print(e)