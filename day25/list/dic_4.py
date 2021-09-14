#디셔너리 에제

dic = {1:'A', 2:'B', 3:'C'}

dic[4] = 'D'
print(dic)

#수정
dic[4] = 'E'
print(dic)

#삭제
dic.pop(2)
print(dic)

#dic 요소 출력
for key in dic:
    print(key)
    print(dic[key])