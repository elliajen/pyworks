from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("http://www.naver.com")
html = BeautifulSoup(url, "html.parser")

"""
div = html.find('div', {'class' : 'service_area'})
first_a = div.find('a')
print(first_a.text)

all_a = div.findAll('a')    # 요소를 전체 리스트로 반환
print(all_a)
print(all_a[1].text)
for i in all_a:
    print(i.text)
"""

ul = html.find('ul', {'class':'list_nav type_fix'})
# ul -> li -> a로 찾아 들어감
"""
all_li = ul.findAll('li')
for li in all_li:   # 전체 출력
    a = li.find('a')
    print(a.text)
"""

#a로 찾기 ul->a
all_a = ul.findAll('a')
for a in all_a:
    print(a.text)

#print(all_li)
#print(all_li[0].text)  # 메일
#print(all_li[1].text)  # 카페
