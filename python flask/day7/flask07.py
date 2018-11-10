from flask import Flask, render_template, request, make_response, redirect, session
import datetime
import os
from flask_sqlalchemy import SQLAlchemy
import pymysql
#将pymysql伪装成mysqldb
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()

app=Flask(__name__)
#flask是创建的库名
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#指定执行完操作后自动提交　
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#创建一个对象
#创建SQLALchemy的实例，并将app指定给实例
#db是SQLAlchemy的实例，表示的是正在使用的数据库，
# 同时db页具备SQLAlchemy中的所有功能　
db=SQLAlchemy(app)

app.config['SECRET_KEY']='dasdsadsadsadsaada'

@app.route('/')
def h():
    return 'hello world'

@app.route('/01-setCookie')
def setCookie():

    resp = make_response('添加cookie成功')
    # 通过resp保存cookie的值到客户端浏览器中　
    resp.set_cookie('qinjianyong','tazuishuai',36000000)
    return resp


@app.route('/02-getcookie')
def gerCookie():
    print(request.cookies)
    print(request.cookies.get('qinjianyong'))
    return '帅'

@app.route('/03-setSession')
def setSession():
    session['uname'] = 'Mrwang'
    return 'set session success'

@app.route('/04-getsession')
def getsession():
    uname=session.get('uname','')
    if uname :
        return '用户名为:'+uname
    else:
        return '无'

#
# @app.route('/05-login',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         uname = session.get('uname','')
#         if uname:
#             return '回到首页'
#         else:
#             upwd = request.cookies.get('password')
#             if upwd:
#                 session['password'] = upwd
#                 return render_template('回到首页')
#             else:
#                 return render_template('/05-login.html')
#     else:
#         uname = request.form['uname']
#         upwd = request.form['upwd']
#         remenber = request.form['remenber']
#         session['uname'] = uname
#         session['password'] = upwd
#         resp = make_response('返回首页')
#         resp.set_cookie('password',upwd,36000000)
#         return resp

@app.route('/login',methods=['GET','POST'])
def xxx():
    if request.method == 'GET':
        #判断是否已经在登录状态，判断session中是否右uname的值
        if 'uname' in session:
            #已经等路，直接去网首页
            return redirect('/')
        else:
            #没有等路，继续向下判断cookie
            if 'uname' in request.cookies:
                #层金记住过密码，取出值保存金session
            uname = request.cookies.get('uname')
            session['uname'] = uname
            return redirect('/')
            else:
                # 之前没有登录过，去往登录页
                return render_template('login.html'   )

        return render_template('login.html')
    else:
        #显出里登录，登录成功则保存金session
        uname= request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname == 'admin' and upwd == 'admin':
            #先声明重定向的对象
            resp = redirect('/')
            #登录成功　: 先将数据保存进session
            session['uname'] = uname
            #是否要记住密码
            if 'isSaved' in request.form:
                #需要记住用户名，将信息保存进cookie
                resp.set_cookie('uname',uname,36000000)

            return resp

        else:
            #登陆失败
            return redirect('/login')















if __name__ == '__main__':
    app.run(debug=True)