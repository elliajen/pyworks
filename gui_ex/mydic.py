# 방향 - W(west),E(east),S(south),N(north)
from tkinter import *


def click():
    try:
        word = entry.get()  #입력된 단어를 가져와서
        definition = dic[word]  #단어로 정의를 검색
    except KeyError:
        text.insert(END, "정의를 찾을 수 없습니다.")
    text.delete(0.0, END)
    text.insert(END, definition)    #정의를 출력 상자에 넣는다.

root = Tk()
root.title("용어사전")

Label(root, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요").grid(row=0, column=0, sticky=W)
entry = Entry(root, width=20, bg="pink")
entry.grid(row=1, column=0, sticky=W)
Button(root, text="확인", command=click).grid(row=2, column=0, sticky=W)
Label(root, text="정의 : ").grid(row=3, column=0, sticky=W)
text = Text(root, width=100, height=5, bg="pink")
text.grid(row=4, column=0, sticky=W)


dic = {
    "이진수" : "2진법으로 나타낸 숫자, 0과 1로 구성됨",
    "html" : "하이퍼텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.",
    "함수" : "재사용 가능한 코드 조각이다. function 이라고 한다.",
    "버그" : "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각이다."
}



root.mainloop()