# raise 구문 - 예외처리를 미뤄놓음
# 사용하는 쪽에서 예외처리를 사용해야함
class Animal:
    def cry(self):
        raise NotImplementedError   # 상속받는 클래스가 반드시 구현해야함
    def breath(self):
        print("숨을 쉽니다.")

class Dog(Animal):
    # pass
    def cry(self):
        print("멍!멍!")

class Cat(Animal):
    def cry(self):
        print("냥~냥~")

dog = Dog() # 상속
dog.cry()   # 부모 메서드 사용
dog.breath()

cat = Cat()
cat.cry()
cat.breath()