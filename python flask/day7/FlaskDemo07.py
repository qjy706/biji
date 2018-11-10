from flask import Flask, make_response, request, session, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY']='aixieshaxiesha,yuefuzayuehao%$'


@app.route('/01-setCookie')
def setCookie():
    resp = make_response('添加cookie成功')
    # 通过resp 保存cookie的值到客户端浏览器中
    resp.set_cookie('uname','jack',60*60*24*365)
    return resp
@app.route('/02-getCookie')
def getCookie():
    # print(request.cookies)
    print(request.cookies.get('uname'))
    return "获取cookies成功"


@app.route('/03-setSession')
def setSession():
    session['uname'] = 'MrWang'
    return "Set Session Success"
@app.route('/04-getSession')
def getSession():
    uname = session.get('uname','')
    if uname:
        return "用户名为:"+uname
    else:
        return "没找到相关信息"

@app.route('/')
def index():
    return "欢迎来到首页"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # 判断是否已经在登录状态上:判断session中是否有uname的值
        if 'uname' in session:
            # 已经登录了，直接去往首页
            return redirect('/')
        else:
            # 没有登录，继续向下判断cookie
            if 'uname' in request.cookies:
                # 曾经记住过密码,取出值保存进session
                uname = request.cookies.get('uname')
                session['uname'] = uname
                return redirect('/')
            else:
                #　之前没有登录过,去往登录页
                return render_template('login.html')
    else:
        #先处理登录,登录成功继续则保存进session,否则回到登录页
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname=='admin' and upwd=='admin':
            # 声明重定向到首页的对象
            resp = redirect('/')
            # 登录成功：先将数据保存进session
            session['uname'] = uname
            # 判断是否要记住密码
            if 'isSaved' in request.form:
                # 需要记住密码，将信息保存进cookie
                resp.set_cookie('uname',uname,60*60*24*365)
            return resp
        else:
            # 登录失败
            return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
