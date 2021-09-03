#*로 삼각형 만들기
for i in range(0, 5):
    for j in range(0, 5):
        print('*', end=" ")
    print()
    
print()

for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end=" ")
    print()
    
print()

for i in range(0, 5):
    for j in range(0, 5-i):
        print('*', end=" ")
    print()

for i in range(0, 5):
    for j in range(0, 4-i):
        print(' ', end=' ')
    for j in range(0, i+1):
        print('*', end=' ')
    print()
