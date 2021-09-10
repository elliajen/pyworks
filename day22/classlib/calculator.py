class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalcurator(Calculator):
    def minus(self, val):
        self.value -= val

"""
cal1 = Calculator()
print(cal1.value)
"""

cal2 = UpgradeCalcurator()
cal2.add(10)
cal2.minus(7)

print(cal2.value)