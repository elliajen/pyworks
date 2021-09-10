class Calculator:
    def __init__(self):
        self.valeu = 0

    def add(self, val):
        self.valeu += val
        return self.valeu

class UpgradeCalculator(Calculator):
    def minus(self, cal):
        self.valeu -= cal

    cal = UpgradeCalculator()
    cal.add(15)
    cal.minus(6)

print(cal.value)