from flask import  Flask

#将当前运行的主程序构建成flask应用，以便接收用户请求(request)并给出响应（response)
app = Flask(__name__)


#@app.route() Flask中的路由定义 主要定义用户的访问路径　'/'表示整个网站的根路径　
#def index() 表示的是匹配上@app.route()路径后的处理程序　－　视图函数 所有视图函数必须要有return
#return 后面可以是一个字符串也可以是一个独立的响应对象　
@app.route('/')
def index():
    return '<h1>我的第一个flask程序</h1>'


#访问地址　http://localhost:5000/show/xxx

@app.route('/show/<name>')
def show(name):
    return '%s'%name


@app.route('/show/<name>/<int:age>')
def show_age(name,age):
    return '%s %d'%(name,age)






if __name__ == '__main__':
    #运行flask应用(启动flask服务),默认在本机开启端口是5000
    #debug = True 将启动模式更改为调试模式　会在页面中提示错误信息　不写就不会出现错误信息,开发环境时推荐写true　生产时false
    app.run(debug=True,port=5555)