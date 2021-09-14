# a모드는 주로 input() 코드에서 필수 사용.
#연산은 문자열 포메팅 방식으로 가능하다.
f = open("c:/pyfile/number2.txt", 'a')
f.write("%d\n" % (100/2))
f.write("%.2f\n" % 7.34)    #원의 넓이 괄호 ()에 포함해야함
num = "%d\n" % 150000  #변수로 저장
f.write(num)
f.write("%d\n" % 7)
f.close()