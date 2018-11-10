from flask import Flask,render_template,url_for,request


app = Flask(__name__)


@app.route('/01-xhr')
def xhr():
    return render_template('01-xhr.html')


@app.route('/02-ajax-get')
def ajax():
    return render_template('02-ajax-get.html')


@app.route('/02-server')
def server02():
    return '这是我的第一个ajax请求'


@app.route('/03-lianxi',methods=['GET','POST'])
def lianxi():
    return render_template('03-lianxi.html')

@app.route('/03-server')
def server03():
    uanme = request.args.get('uname')
    return '欢迎:%s' % uname


@app.route('/04-post')
def post():
    return render_template('04-post.html')

@app.route('/04-server',methods=['POST'])
def server04():
    uname = request.form['uname']
    age = request.form['age']
    return '姓名:%s,年龄:%s'%uname,age



if __name__ == '__main__':
    app.run(debug=True)