# 주민번호 뒷자리를 -*******로 처리하기

import re

data = '''
kim 871212-1234567
won 930202-1234567
'''
p = re.compile("(\d{6})[-]\d{7}")
s = p.sub("\g<1>-*******", data)

print(s)