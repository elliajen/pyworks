#대입연산자를 활용하여 변수교환
blue = 1
red = 2
print("교환전 : ")
print("blue =", blue, ", red =", red)

#교환처리
#여러줄 주석할떄는 쌍따움표를 3개
"""
yellow = blue
blue = red
red = yellow
"""

#임시 변수 없이 바로 맞교환
blue, red = red, blue

print("교환후 : ")
print("blue =", blue, ", red =", red)
