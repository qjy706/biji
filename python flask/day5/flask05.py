from flask import Flask,render_template,request,make_response,redirect
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

#创建模型类　-Models
#创建Users类，映射到数据库中叫User表　
#创建字段，id　主键　和自增
#创建字段　username,长度为80的字符串，不允许为空　值必须唯一
#创建字段:age,整数　允许为空
#创建字段　email,长度为120的字符串　必须唯一　



class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age=db.Column(db.Integer,nullable=True)
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Users:%r>' % self.username


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)

class course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30),nullable=False)



@app.route('/01-insert')
def insert_views():
    #创建Users对象并赋值　
    # users = Users('王老师', 32, 'wangWC')
    # #将对象通过db.session.add()插入到数据库　
    # db.session.add(users)
    # #提交插入操作
    # db.session.commit()

    users = Users('魏老师',40,'666@163.com')
    db.session.add(users)

    return 'Insert Success'


@app.route('/02-register',methods=['GET',"POST"])
def register_views():
    if request.method == "GET":
        return render_template('02-register.html')
    else:
        uname = request.form['uname']
        uage = request.form['uage']
        uemail = request.form['uemail']
        users = Users(uname, uage, uemail)
        db.session.add(users)
        return 'qjy is a good man'


@app.route('/03-query')
def query_views():
    #测试query()函数
    print(db.session.query(Users))
    # 返回的是里面的每一个对象　　对象的属性就是里面存储的信息 self.xxx=xxx
    print(db.session.query(Users.username))
    query = db.session.query(Users)
    print(query.all())
    #[<Users:'王老师'>, <Users:'魏老师'>, <Users:'秦'>]
    # #返回的是一个列表 遍历之后是每一个实体　实体就是对象　对象的属性就是字段　
    # for user in query.all():
    #     print(user)
    #     print('姓名:{},年龄:{},邮箱:{}'.format(user.username,user.age,user.email))
    #
    # #查询执行函数
    f=query.first()
    print(f)

    #count
    c = query.count()
    print(c)

    #查询过滤器函数　filter
    #查询年龄大于25的用户的信息　
    # result=db.session.query(Users).filter(Users.age>25).all()
    result = db.session.query(Users).filter(Users.age > 25,Users.id>1).all()
    print(result)

    a=db.session.query(Users).filter(or_(Users.age > 30,Users.id > 1)).all()
    print(a)

    h=db.session.query(Users).filter(Users.username == '魏老师').all()
    print(h)
    likes = db.session.query(Users).filter(Users.email.like('%@%')).all()
    print(likes[0].age)

    c = db.session.query(Users).filter(Users.id.in_([2,3])).all()
    print(c)

    #查询Users所有人年龄综合　聚合函数
    fun_sum = db.session.query(func.sum(Users.age).label('sum_age')).all()
    print(fun_sum)

    C = db.session.query(Users).limit(1).all()
    print(C)

    #使用order_by 年龄升序　id降序
    D=db.session.query(Users).order_by('age asc,id desc').all()
    print(D)
    return 'Query OK'



@app.route('/03-queryall')
def queryall():
    #Users类中所有的数据　也就是表里面所有的数据
    query = db.session.query(Users).all()
    print(query)
    return render_template('03-queryall.html',users=query)



@app.route('/04.update',methods=['GET',"POST"])
def update():
    if request.method == 'GET':
        id = request.args.get('uname')

        # print('{}'.format(name))
        # print(type(name))
        # query=db.session.query(Users).all()
        # for x in query:
        #     print(type(x.username))
        #     print(x.username)
        #     if name == x.username:
        #         print('666')
        query = db.session.query(Users).filter_by(id = id).all()
        obj = query[0]
        print(obj.id)
        print(query)
        #返回的是一个列表
        # obj = query[0]
        # print(query.age)
        return render_template('04-update.html',info=obj)
    else:
        #接收前端传递过来的四个值 id username age email
        id = request.form.get('id')
        username = request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        #一查　二改　三保存 根据id查询出对应的信息
        user = Users.query.filter_by(id=id).first()
        user.username = username
        user.age = age
        user.email = email
        db.session.add(user)
        return redirect('/03-query')
        #将username,age,email的值分别赋值给user对应的属性　
        #响应　: 重定向回/03-queryall



@app.route('/05-query')
def query05_views():
    #使用models查询数据
    user=Users.query.filter(Users.id==1).first()
    print(user)
    return 'Query OK'


@app.route('/06-delete')
def update_views():
    id = request.args.get('id')
    print(id)
    user=Users.query.filter_by(id=id).first()
    print(user)
    db.session.delete(user)
    return redirect('/03-queryall')



























#删除一床间的表结构
# db.drop_all()

#将创建好的实体类映射回数据库
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)