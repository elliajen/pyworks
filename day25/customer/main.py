from member import Customer, GoldCustomer, VipCustomer

#Customer 객체(인스턴스) 생성
c1 = Customer(101, "이예린")
c2 = Customer(102, '박주리')
g1 = GoldCustomer(201, "홍서형")
g2 = GoldCustomer(202, "원주희")
v1 = VipCustomer(301, "선우여", 777)
#상품구매
price = 10000
c1.calc_price(price)
c2.calc_price(price)
g1.calc_price(price)
g2.calc_price(price)
v1.calc_price(price)

#고객정보 출력
c1.showInfo()
c2.showInfo()
g1.showInfo()
g2.showInfo()
v1.showInfo()