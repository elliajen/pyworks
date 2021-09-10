class Airplane:
    # 기본 생성자는 생략 가능
    def __init__(self):
        pass

    def takeoff(self):
        print("비랭기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반비행합니다.")
    def lan(self):
        print("비행기가 착륙합니다.")

class SuperSonicPlane(Airplane):
    NOMAL = 1       # 상수는 관례상 대문자 표기
    SUPERSONIC = 2

    def __init__(self):
        self.flymode = SuperSonicPlane.NOMAL    # 상수도 클래스 이름으로 접근

        def fly(self):
            if self.flymode == SuperSonicPlane.SUPERSONIC:
                print("비행기가 초음속 비행을 합니다.")
            else:
                super().fly()   # 부모 메서드 상속 시에 super()로 받음

sa = SuperSonicPlane()
sa.takeoff()
sa.fly()
sa.flymode = SuperSonicPlane.SUPERSONIC
sa.fly()
sa.flymode = SuperSonicPlane.NOMAL
sa.fly()
sa.lan()

