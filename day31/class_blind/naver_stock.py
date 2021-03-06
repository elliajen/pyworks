# 네이버 > 증권 > 금융홈 > 우측 삼성전자
from urllib import request
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = request.urlopen("https://finance.naver.com/item/main.naver?code=" + item_code)
    html = BeautifulSoup(url, "html.parser")
    #content = html.find('p', {'class' : 'no_today'})
    content = html.select_one('p.no_today') # 태그이름.클래스이름
    print(content)
    return content

def getprice(item_code):
    content = getcontent(item_code)
    #price = content.find('span', {'class':'blind'})
    price = content.select_one('span.blind')
    return price

삼성전자 = getprice('005930')
카카오 = getprice('035720')
네이버 = getprice('035420')

print("삼성전자 주가 : {}원". format(삼성전자.text))
print("카카오 주가 : {}원". format(카카오.text))
print("네이버 주가 : {}원". format(네이버.text))