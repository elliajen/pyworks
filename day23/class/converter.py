# 단위변환 클래스- 1inch->25.4mm
class ScaleConverter:
    def __init__(self,units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor * val

c = ScaleConverter("inch", 'mm', 25)
print("inch 를 mm로 변환 ==")
print("1인치는 " + str(c.convert(1)) + c.units_to)

c2 = ScaleConverter("KB", "Byte", 1024)
print("KB를  Byte 로 변환")
print("1KB는 " + str(c2.convert(1)) + c2.units_to)