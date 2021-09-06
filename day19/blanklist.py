#리스트 함수

n = []  # 비어있는 n리스트 선언


print("요소 추가")
print()
print("- append()")
n.append(90)
n.append(80)
n.append(70)
n.append(60)
print(n)
n.append(100)
print(n)

print("- insert()")
n.insert(1,50)  #1번 인덱스에 50 추가
print(n)

print('='*20)

print("요소 삭제")
print()
print("- pop()")
n.pop()   #맨 뒤에서 삭제
print(n)

print("- remove()")
n.remove(80)    #특정요소 삭제
print(n)

print('='*20)

print("정렬")
print()
print("- reverse() : 순서 거꾸로 뒤집기")
n.reverse()
print(n)

print("sort() : 오름차순")
n.sort()
print(n)


