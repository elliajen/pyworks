# 객체(인스턴스)를 리스트로 관리
from member import Customer, GoldCustomer, VipCustomer

# Customer 객체(인스턴스) 생성
c1 = Customer(101, "이예린")
c2 = Customer(102, '박주리')
g1 = GoldCustomer(201, "홍서형")
g2 = GoldCustomer(202, "원주희")
v1 = VipCustomer(301, "선우여", 777)

# 리스트로 관리
customer = []
customer.append(c1)
customer.append(c2)
customer.append(g1)
customer.append(g2)
customer.append(v1)

print("============= 구매가격과 보너스 포인트 계산 =============")
price = 10000   # 상품 - 10000원
for c in customer:
    cost = c.calc_price(price)  # 구매가격(할인적용)
    print(c.getname() + "님의 지불 금액은 " + format(cost, ',d') + "원 입니다.")

print("====================== 고객정보 ======================")
for c in customer:
    c.showInfo()