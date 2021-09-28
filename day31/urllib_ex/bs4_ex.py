# BeautifulSoup 사용하기 - html 태그 및 데이터 추출 라이브러리
from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class="item">
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ul>
        <ul class="lang">
            <li>Python</li>
            <li>C/C++</li>
            <li>Java</li>
        </ul>
    </body>
</html>
"""

# find(), select_oen('개체이름.클래스이름)
html = BeautifulSoup(html_str, "html.parser")
# find() 첫번째 요소를 찾음
# first_ul = html.find('ul')
first_ul = html.select_one('ul')
second_ul = html.select_one('ul.lang')

# print(first_ul) # 태그까지 다 출력
# print(first_ul.text)    # 텍스트만 출력

print(second_ul)
print(second_ul.text)