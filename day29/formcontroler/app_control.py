from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member_list')
def member_list():
    return render_template('member_list.html')

# 회원목록
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uid = request.form['uid']
        passwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        return render_template('member_list.html', uid = uid, passwd = passwd, name = name, age = age)   # 요청대로 처리된 결과 페이지
    else:
        return render_template('register.html')

@app.route('/login', methods = ['GET','POST'])   # post방식
def login():
    if request.method == 'POST':
        uid = request.form['uid'] # name 값을 가져옴
        passwd = request.form['passwd']
        return render_template('index.html', uid = uid, passwd = passwd)
    else:
        return render_template('login.html')

# 짝수/홀수 판정 프로그램
@app.route('/even_odd', methods=['GET','POST'])
def even_odd():
    if request.method == 'POST':
        try:
            num = int(request.form['num'])  #입력된 숫자를 받아옴
        except ValueError:
            error_message = "숫자를 입력해주세요"
            return render_template('even_odd.html', error_message=error_message)
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render_template('result.html', num=num, result=result)
            # 딕셔너리의 key=value 구조임
    else:
        return render_template('even_odd.html')
app.run()