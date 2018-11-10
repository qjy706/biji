from flask import  Flask,render_template,url_for,request

app = Flask(__name__)


@app.route('/01-static')
def static_views():
    # url = url_for('static',filename='images/alipay.jpg')
    # print(url)
    return render_template('01-static.html')


#访问路径　http://localhost:5000/02-parent
@app.route('/02-parent')
def parent_views():
    return  render_template('02-parent.html')

#访问路径  http://localhost:5000/03-child
@app.route('/03-child')
def child_views():
    return  render_template('03-child.html')

@app.route('/04-request')
def request_views():
    print(request)
    # 获取请求方案
    scheme = request.scheme

    # 获取请求方式　
    method = request.method

    # 获取get请求方式的请求数据
    args=request.args

    # 获取post请求方式的请求数据
    form = request.form

    #获取cookies中的信息　
    cookies = request.cookies

    #获取请求路径(具体资源，不带参数)
    path = request.path

    # 获取请求路径(具体资源，带参数)
    full_path = request.full_path

    # 获取请求路径(完整路径)
    url = request.url

    #获取所有的请求消息头 返回值是字典　
    headers = request.headers

    print(headers)
    #获取User-Agent 请求消息头信息
    ua = request.headers['User-Agent']

    #获取referer请求消息头的信息　取出一个键为Referer 没有值 则赋值空
    # 网页从哪来回哪去就能操作了　

    referer = request.headers.get('Referer','')
    return render_template('04-request.html',params=locals())


#访问地址　http://localhost:5000/05-form-get
@app.route('/05-form-get')
def form_get():
    return  render_template('05-form-get.html')

@app.route('/06-get')
def get_view():
    print(request.args)
    uname = request.args['uname']
    upwd = request.args['upwd']
    print('uname:%s,upwd:%s'%(uname,upwd))
    return 'Get Success'


@app.route('/07-form-post',methods=['POST','GET'])
def form_post ():
    if request.method == 'GET':
        return render_template('07-form.html')
    else:
        print(request.form)
        uname = request.form['uname']
        upwd = request.form['upwd']
        utruename = request.form['utruename']
        uemail = request.form['uemail']
        return render_template('07-post.html', params=locals())

#
# @app.route('/07-post')
# def post():
#     uname = request.form['uname']
#     upwd = request.form['upwd']
#     utruename = request.form['utruename']
#     uemail = request.form['uemail']
#     return render_template('07-post.html',params=locals())


if __name__ == '__main__':
    app.run(debug=True,port='7777',host='0.0.0.0')