# 중복검사
def find_same_name(li):
    same_name = []
    n = len(li)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if li[i] == li[j]:
                same_name.append(li[j])
    return same_name

"""
1행 li[0]==[li[1], li[0]==[li[2], li[0]==[li[3]"""



name = ['콩쥐', '팥쥐', '심청', '팥쥐', '심청']
print(find_same_name(name))