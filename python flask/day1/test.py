from flask import Flask,url_for
app=Flask(__name__)
@app.route('/html',methods=['post'])
def hello_word():
    return 'post方法'

@app.route('/')
def hello_word_1():
    # x = 10
    # y = 0
    # res = x/y
    return ''' <form action='/html' method='post'> 
                名字：<input type='text' name='name'></input><br\> 
                密码：<input type='passwd' name='passwd'></input><br\> 
                提交：<input type='submit' name='submit'></input> </form> '''

@app.route('/test')
def query_user():
    '''
    http://127.0.0.1:5000/test?id=123
    '''
    # id = request.args.get('id')
    return 'query user:'

@app.route('/query_url')
def query_url():
    '''
    反导出 query_user函数名对应的url地址
    '''
    return 'query url:'+url_for('query_user')

@app.route('/xcz')
def ccc():
    return '6660'

@app.route('/asd')
def info():
    show = url_for('ccc')
    return show



if __name__ == '__main__':
    app.run(debug=True)
