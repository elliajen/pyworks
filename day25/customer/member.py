# 고객 클래스 정의
class Customer:
    def __init__(self, cid, cname):
        self._cid = cid              # 고객 아이디(private - 접근제한)
        self._cname = cname          # 고객 이름
        self.cgrade = "Silver"      # 고객 등급
        self.bonus_point = 0        # 보너스 포인스
        self.bonus_ratio = 0.01     # 보너스 적립율 - 1%

    def getname(self):  # cname이 접근 불가이므로 함수로 가져옴
        return self._cname

    # 보너스포인틑 = 상품가격 x 보너스 적립율
    def calc_price(self, price):
        # 포인트는 정수로 변환하고 누적이 되기 때문에 += 이걸로 표시
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def showInfo(self): #고객정보
        print(self.getname() + "님의 등급은 " + self.cgrade + " 이며,보너스 포인트는 " +
              str(self.bonus_point) + "점 입니다.")

# 클래스 상속
class GoldCustomer(Customer):
    def __init__(self, cid, cname):
        super().__init__(cid, cname)    #Customer 멤버 상속
        self.cgrade = "Gold"  # 고객 등급
        self.sale_ratio = 0.1   # 구매 할인율 - 10%
        self.bonus_ratio = 0.02  # 보너스 적립율 - 2%

    # 매소드 재정의(오버라이드)
    def calc_price(self, price):
        # 할인된가격의 포인트 적립이 아닌 구매한 상품의 가격으로 적립되기 때문에
        # 보너스 포인트 계산을 먼저 하고 그 뒤에 할인가 계산을 해야함
        self.bonus_point += int(price * self.bonus_ratio)
        # 상품가격 = 상품가격 - 할인된 가격
        price = price - int(price * self.sale_ratio)
        return price

# 클래스 상속
class VipCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.agent = agent  #전문 상담원
        self.cgrade = "VIP"  # 고객 등급
        self.sale_ratio = 0.1  # 구매 할인율 - 10%
        self.bonus_ratio = 0.05  # 보너스 적립율 - 5%

    def calc_price(self, price):        #매소드 재정의(오버라이드)
        self.bonus_point += int(price * self.bonus_ratio)
        # 상품가격 = 상품가격 - 할인된 가격
        price = price - int(price * self.sale_ratio)
        return price

    def showInfo(self):
        super().showInfo()
        print(self.getname() + "님께서는 " + self.cgrade+ " 등급으로 전문상담원이 배정되었습니다. 상담원의 아이디는 " +
              str(self.agent) + "입니다.")