from flask import Flask
app=Flask(__name__)
@app.route('/html',methods=['post'])
def hello_word():
    return 'post方法'

@app.route('/')
def hello_word_1():
    return ''' <form action='/html' method='post'> 
                名字：<input type='text' name='name'></input><br\> 
                密码：<input type='passwd' name='passwd'></input><br\> 
                提交：<input type='submit' name='submit'></input> </form> '''

app.run()
