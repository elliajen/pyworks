class ScaleConverter:
    def __init__(self,units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor * val

class Converters(ScaleConverter):
    def __init__(self, units_from, units_to, factor, factor2):
        super().__init( units_from, units_to, factor)
        self.factor2 = factor2
    def convert(self, val):
        return super().convert(val) + self.factor2

conv = Converters('C', 'F', 1.8, 32)
print("20C를 화씨 온도로 변환")
print(str(conv.convert(20)) + conv.units_to)