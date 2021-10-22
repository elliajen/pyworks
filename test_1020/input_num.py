x = input
year = int(x)
yun = 366
poung = 365
day = 365 % 7
if day == 0:
    print("서기", year, "년은 월요일입니다.")
elif day == 1:
    print("서기", year, "년은 화요일입니다.")
elif day == 2:
    print("서기", year, "년은 수요일입니다.")
elif day == 3:
    print("서기", year, "년은 목요일입니다.")
elif day == 4:
    print("서기", year, "년은 금요일입니다.")
elif day == 5:
    print("서기", year, "년은 토요일입니다.")
else:
    print("서기", year, "년은 일요일입니다.")