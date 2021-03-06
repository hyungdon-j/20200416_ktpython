import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# 자동갱신 되도록 설정
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "welcome day7 class 2222"

@app.route("/exam01", methods=['get', 'post'])
def exam01():
    result = ''
    if request.method == 'POST':
        result = request.form['numbers']
        result = [int(s.strip()) for s in result.split(',')]
        min_number = min(result)
        
        if min_number % 2 == 0:
            result = f'가장 작은 수 {min_number}는 짝수'
        else:
            result = f'가장 작은 수 {min_number}는홀수'
        
    return render_template('base.html', 
                           title="가장 작은 수 찾기",
                           result=result,
                           site="exam01",
                           placehoder="num1, num2, num3")

@app.route('/daum')
def daum():
    res = requests.get('http://daum.net')
    return res.text.replace('https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png', 'https://ssl.pstatic.net/sstatic/search/nlogo/20200421102755.png')

@app.route('/pub/<sub>')
def daum_sub(sub):
    res = requests.get(f'http://daum.net/pub/{sub}',
                       params=request.args)
    return res.text

# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 
# 해당 숫자에 대한 구구단을 출력하세요.
@app.route('/gugu', methods=['get', 'post'])
def gugu():
    result = []
    if request.method == 'POST':
        number = int(request.form['numbers'].strip())
        for i in range(9):
            result.append(f'{number} * {i + 1} = {number * (i + 1)}')
        
    return render_template('base.html', 
                           title="구구단 출력하기",
                           result="<br>".join(result),
                           site="gugu",
                           placehoder="num")

# 사용자로부터 숫자를 N을 입력받은 후 
# 1부터 N까지의 숫자 중 3의 배수만 출력하세요.
@app.route('/multiple', methods=['get', 'post'])
def multiple():
    result = ''
    if request.method == 'POST':
        num = int(request.form['numbers'].strip())
        result = [str(i) for i in range(1, num + 1) if i % 3 == 0]
        
    return render_template('base.html', 
                           title="3의 배수 출력하기",
                           result=','.join(result),
                           site="multiple",
                           placehoder="num")

# *트리 출력
@app.route('/tree', methods=['get', 'post'])
def tree():
    # "&nbsp;"
    result = []
    for i in range(5):
        row = ""
        for j in range(i + 1):
            row += '*'
        result.append(row)
    
    return render_template('base.html', 
                           title="* 트리 출력하기",
                           result="<br>".join(result),
                           site="tree",
                           placehoder="num")

# 금지어 체크
@app.route('/reject', methods=['get', 'post'])
def reject():
    금지어 = ['볼드모트', '이숙번', '강두루', '이고잉']
    result = ''
    
    if request.method == 'POST':
        # 문자열을 text 변수에 받아서
        text = request.form['numbers']
        
        # 금지어 목록에서 하나씩 단어를 가져와서 
        for word in 금지어:
            # 금지어를 *** 로 replace
            text = text.replace(word, '***')
            
        result = text
    
    return render_template('base.html', 
                           title="금지어 체크하기",
                           result=result,
                           site="reject",
                           placehoder="문장을 입력해 주세요")


# python 파일명으로 실행을 위해서 필요
app.run(port=8001)