# 장바구니 class
class Cart:
    # class 빈 리스트 선언
    li = []

    def __init__(self, goods):
        # 클래스 이름으로 접근
        Cart.li.append(goods)

    def __str__(self):
        print(Cart.li)

c1 = Cart("계란")
print(c1.li)
c2 = Cart("우유")
print(c2.li)
c3 = Cart("설탕")
print(c3.li )