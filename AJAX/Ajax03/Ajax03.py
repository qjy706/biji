import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/ajax"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)


class Province(db.Model):
  __tablename__ = 'province'
  id = db.Column(db.Integer,primary_key=True)
  proName = db.Column(db.String(30),nullable=False)
  cities=db.relationship('City',backref='Province',lazy='dynamic')

  def to_dict(self):
    dic = {
      'id':self.id,
      'proName':self.proName
    }
    return dic

class City(db.Model):
  __tablename__ = 'city'
  id=db.Column(db.Integer,primary_key=True)
  cityName=db.Column(db.String(30))
  pid=db.Column(db.Integer,db.ForeignKey('province.id'))

  def to_dict(self):
    dic = {
      "id":self.id,
      "cityName":self.cityName,
      "pid":self.pid,
    }
    return dic

class Users(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer,primary_key=True)
  loginname=db.Column(db.String(30))
  loginpwd = db.Column(db.String(30))
  username = db.Column(db.String(30))


db.create_all()

@app.route('/')
def hello_world():
  return 'Hello World!'

# 返回所有省份所组成的json字符串
@app.route('/01-province')
def province():
  provinces = Province.query.all()
  list = []
  for pro in provinces:
    list.append(pro.to_dict())
  return json.dumps(list)

@app.route('/01-city')
def city():
  pid = request.args.get('pid')
  cities = City.query.filter_by(pid=pid).all()
  list = []
  for c in cities:
    list.append(c.to_dict())
  return json.dumps(list)

@app.route('/02-server',methods=['GET','POST'])
def server02():
  name = request.form.get('name')
  age = request.form.get('age')
  return "姓名:%s,年龄:%s" % (name,age)

@app.route('/03-jq-get')
def jq_get():
  provinces = Province.query.all()
  list = []
  for pro in provinces:
    list.append(pro.to_dict())
  return json.dumps(list)

@app.route('/04-jq-post',methods=['POST'])
def jq_post():
  #1.接收前端传递过来的参数
  lname = request.form.get('loginname')
  lpwd = request.form.get('loginpwd')
  uname = request.form.get('username')
  #2.将参数构建成Users的对象
  user = Users()
  user.loginname = lname
  user.loginpwd = lpwd
  user.username = uname
  #3.将对象保存回数据库
  try:
    db.session.add(user)
    dic = {
      'status':1,
      'msg' : '注册成功'
    }
  except Exception as e:
    print(e)
    dic = {
      'static':0,
      'msg' : '注册失败'
    }
  return json.dumps(dic)

@app.route('/07-crossdomain')
def crossdomain():
  #接收前端传递过来的 callback 的参数
  #callback参数值是指定前端执行处理数据的函数名
  cb = request.args.get('callback')
  return cb+"('这是/07-crossdomain访问路径')"

@app.route('/08-flight')
def flight_views():
  cb = request.args.get('callback')
  dic = {
    'flightNO':'MU763',
    'start':'BeiJing',
    'end':'Saipan',
    'time':'16:55',
  }
  return cb+"("+json.dumps(dic)+")"


if __name__ == '__main__':
  app.run(debug=True)

