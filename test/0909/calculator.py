#계산기 class
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()
cal.add(15)
cal.minus(5)
print(cal.value)

# add() 함수에서 객체 변수가 100이상의 값을 가질수 없도록 제한하는 클래그
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
        return self.value

cal1 = MaxLimitCalculator()
cal1.add(50)
cal1.add(60)
print(cal1.value)