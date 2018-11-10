from flask import Flask,render_template,request,make_response,redirect
import datetime
import os
from flask_sqlalchemy  import SQLAlchemy

app=Flask(__name__)

#为app指定数据库的配置信息　 一组字符串　 说明连接到musql数据库　
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#创建SQLALchemy的实例，并将app指定给实例
#db是SQLAlchemy的实例，表示的是正在使用的数据库，
# 同时db页具备SQLAlchemy中的所有功能　
db=SQLAlchemy(app)


@app.route('/01-js')
def js_views():
    return render_template('01-js.html')

@app.route('/02-get')
def get_views():
    name=request.args['name']
    print(type(name))
    age = request.args['age']
    return '姓名:{},年龄:{}'.format(name,age)

@app.route('/03-response')
def response_views():
    # resp = make_response('这是使用响应对象创建的内容')
    resp=make_response(render_template('01-js.html'))
    return resp

@app.route('/04-redirect')
def redirect_views():
    # 通过重定向的方式交给03-response
    #     跟url_for区别
    # url=url_for('response_views') 再用超链接跳转　
    return redirect('/03-response')

@app.route('/05-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('05-file.html')
    else:
        #获取上传的文件　
        f = request.files['uimg']
        #将上传的文件保存至指定的目录处 先获取上传的文件名
        #将文件名修改为当前时间作为名称　再上传

        #获取运行这个程序时候的时间　精确到毫秒
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

        #获取文件的扩展名
        # filename = f.filename

        ext = f.filename.split('.')[1]

        filename = ftime+'.'+ext

        print(filename)
        # f.save('static/updata/' + filename)

        #将上传的文件保存至指定目录处[绝对路径]
        # dirname是去掉文件名，返回一个目录 dirname(__file__)当前文件的绝对路径
        basedir = os.path.dirname(__file__)
        print('当前文件地址:{}'.format(__file__))
        print(basedir)
        upload_path=os.path.join(basedir,'static/updata',filename)
        print(upload_path)
        f.save(upload_path)

        return 'Upload OK'











if __name__ == '__main__':
    app.run(debug = True,port='8000')