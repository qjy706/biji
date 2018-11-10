from flask import Flask,render_template,request,url_for,redirect,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
pymysql.install_as_MySQLdb()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/ajax'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(30))
    loginpwd = db.Column(db.String(30))
    uname = db.Column(db.String(30))

    def __repr__(self):
        return '<用户名称:%r>'%self.uname

    # 如果想要去客户端以json格式发挥　需要创建一个方法把对象转换成字典
    def to_dict(self):
        dic = {
            'id':self.id,
            'loginname':self.loginname,
            'loginpwd' : self.loginpwd,
            'uname':self.uname
        }
        return dic
db.create_all()



#现在需要用通过ajax访问数据库　得到全部数据　

@app.route('/01-allUsers')
def User():
    return render_template('01-allusers.html')

@app.route('/01-server')
def server01():
    users = Users.query.all()
    print(users)
    return users



@app.route('/02-json')
def json_views():
    list = ['fan bing bing','范冰冰','li chen','李晨']
    dict = {
        'name':"fan bing bing",
        'age' : 37,
        'gender' : 'female'
    }

    ulist = [{
        'name': "wang",
        'age': 37,
        'gender': 'male'
    },
        {
            'name':'qin',
            'age':15,
            'gender':'male'
        }


    ]

    jsonStr=json.dumps(ulist)
    return jsonStr


@app.route('/02-html')
def html_view():
    return render_template('02-josn.html')


@app.route('/03-users')
def user():
    return render_template('03-users.html')


@app.route('/03-server')
def server():
    user = Users.query.filter_by(id=1).first()
    # 想要被JSON识别　需要单独设置一个对象属性　
    user = user.to_dict()
    print(user)
    # user.name取值
    #是一个列表
    return json.dumps(user)

@app.route('/04')
def flask():
    return render_template('04-lianxi.html')


@app.route('/04-lianxi')
def lianxi():
    lusers = Users.query.all()
    list = []

    for l in lusers:
        list.append(l.to_dict())
    return json.dumps(list)


@app.route('/04-del')
def xxx():
    # 先获取前段传递过来的id值
    id = request.args.get('id')
    user = Users.query.filter_by(id=id).first()
    try:
        db.session.delete(user)
        dic ={
            'status':1,
            'msg' : '删除成功'
        }
    except Exception as e :
        print(e)
        dic ={
            'status':0,
            'msg' : '删除失败'
        }
    return json.dumps(dic)











if __name__ == '__main__':
    app.run(debug=True)