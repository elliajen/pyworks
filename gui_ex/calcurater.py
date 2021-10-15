from tkinter import *

def click1(key):
    if key == '=':
        display.insert(END, key)
    elif key == 'C':
        display.delete(0, END)

root = Tk()
root.title("계산기")
root.geometry("150x100+300+200")
frame = Frame(root)
frame.pack()

display = Text(frame, width=20, height=1)    # 출력상자
display.grid(row=0, column=0)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C'
]
r = 0
c = 0
for btn_txt in operator_list:
    def cmd(x=btn_txt):
        click(x)
    Button(operator, text=btn_txt, width=5, command=cdm).grid(row=r, column=0)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

Button(frame, text="1", width=3, command=click1).grid(row=1, column=0)
Button(frame, text="2", width=3, command=click2).grid(row=2, column=0)

root.mainloop()