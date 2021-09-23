import os
import glob

os.chdir('c:/webdev/pyworks')   # webdev 폴더로 이동
dir = os.popen('dir')         # 'dir' 명령 실행
#print(dir.read())

# glob 모듈로 file_io의 파일이름 알아내기 - txt 파일 읽어오기
data = glob.glob("c:/webdev/pyworks/day28/file_io/*.txt")
print(data) # 리스트 형태로 반환

# animal.txt 읽기
with open("c:/webdev/pyworks/day28/file_io/animal.txt", 'r') as content:
    data = content.read()
    print(data)