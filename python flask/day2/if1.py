from flask import  Flask,render_template,url_for

app = Flask(__name__)

@app.route('/03-if')
def index():
    uname = 60
    return render_template('03-if.html',params = locals())


@app.route('/user/login')
def login():
    return '模拟登录地址'

@app.route('/04-for')
def for1():
    list = ['孙悟空','猪八戒','周瑜','鲁班七号','孙尚香']
    dic = {
        'SWK':'孙悟空',
        'PJL':'潘金莲',
        'XMQ':'西门庆',
        'WDL':'武大郎'}

    return render_template('04-for.html',params=locals())

@app.route('/05-static')
def asd():
    return render_template('05-head.html')


if __name__ == '__main__':
    app.run(debug=True,port=9000)