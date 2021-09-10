# person 클래스

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person):
    pass
# Person 을 상속받음 자식클래스 이름(부모클래스)

#main
# p1(인스턴스, 객체)
p1 = Person("손흥민", 30)
print(p1.name, p1.age)
p2 = Person("김연아", 26)
print(p2)


# 상속받은 Employee 객체 생성하기
emp1 = Employee("흥부", 30)
emp1.name
print(emp1.name)    # name / age는 Person의 소속인데 Employee 객체가 사용
print(emp1.age)
print(emp1)

emp2 = Employee("놀부", 35)
print(emp2)


"""
p1 = Person("흥부", 29)
print(p1)
"""