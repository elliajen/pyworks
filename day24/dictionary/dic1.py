# 딕셔너리 자료구조
# 키와 값으로 이루어짐

person = {}  #빈 딕셔너리 선언

# 요소 추가
person['name'] = '장그래'
person['age'] = 29
person['phone'] = '010-2424-3535'
person['gender'] ='남자'
print(person)

del person['age']  #age 요소 삭제
print(person)

person['name'] = '오상식' #요소 수정
print(person)