from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/ajax'
#指定执行完操作后自动提交　
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
db.create_all()

@app.route('/01-register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('01-register.html')
    else:
        loginname = request.form['lname']
        loginpwd = request.form['upwd']
        uname = request.form['uname']
        user = Users()
        user.loginname = loginname
        user.loginpwd = loginpwd
        user.uname = uname
        db.session.add(user)
        return 'ok'




@app.route('/02-server')
def server():
    loginname = request.args.get('loginname')
    x = Users.query.filter_by(loginname=loginname).first()
    if x:
        return '该值存在'
    else:
        return '通过'






if __name__ == '__main__':

    app.run(debug=True)

