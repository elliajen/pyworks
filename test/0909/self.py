x = input("전체 수 : ")
customer_num = int(x)
y = input("열수 : ")
col_num = int(y)

if customer_num % col_num == 0:
    row_num = int(customer_num / col_num)
else:
    row_num = int(customer_num / col_num)+1
print(str(row_num) + "개의 줄이 필요합니다.")