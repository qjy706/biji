from flask import Flask
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

@app.route('/<int:666>')
def hey():
    return url_for()


if __name__ == '__main__':
    app.run(debug=True)
