# person 클래스

class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    def __str__(self):
        return "이름 : {0}, 나이 : {1} 월급 : {2}".format(self.name, self.age, self.money)

class Employee(Person): # Person을 상속받음
    pass

emp1 = Employee("흥부", 30, "2,500,000원")
emp1.name
print(emp1.name)    #name / age는 Person의 소속인데 Employee 객체가 사용
print(emp1.age)
print(emp1.money)
print(emp1)


"""
p1 = Person("흥부", 29)
print(p1)
"""