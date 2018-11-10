from flask import Flask

app = Flask(__name__)

#http://locakhost:5000/login  /代表http://localhost:5000/
@app.route('/register')
def register():
    return '<h1>欢迎访问注册页面</h1>'

if __name__ == '__main__':
    #运行flask应用(启动flask服务),默认在本机开启端口是5000
    #debug = True 将启动模式更改为调试模式　开发环境时推荐写true　生产时false
    app.run(debug=True)