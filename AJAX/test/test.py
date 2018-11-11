from flask import Flask,redirect,render_template,make_response,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/ajaxtest'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.String(30))
    #设置关联属性　学生是一表
    #　一对多　多对多的关联属性　都是列表形式的　可以一次性添加多个对象　
    parents = db.relationship('Parents',backref='childs',lazy='dynamic')

    def __repr__(self):
        return "<student:%r>"%self.sname

    def to_dict(self):
        dic={
            'sname':selfsname,
            'sage':selfsage
        }
        return dic

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.String(30))
    #students是一个列表　可以用append方法添加数据　
    students= db.relationship('Student',secondary='student_teacher',lazy='dynamic',
                              backref=db.backref('teachers',lazy='dynamic'))

    def __repr__(self):
        return "<teacher:%r>"%self.tname

    def to_dict(self):
        dic={
            'tname':selftname,
            'tage':selftage
        }
        return dic


class Parents(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer,primary_key=True)
    pname = db.Column(db.String(30))
    page = db.Column(db.String(30))
    child_id = db.Column(db.Integer,db.ForeignKey('student.id'))

    def __repr__(self):
        #%r是一个对象　跟%s的最大区别
        return '<parent:%r>'%self.pname

student_teacher = db.Table(
    'student_teacher',
    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
    db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id'))

)

db.create_all()

@app.route('/')
def register_teacher():
    t1 = Teacher()
    t2 = Teacher()
    t3 = Teacher()
    t4 = Teacher()
    t5 = Teacher()
    t1.tname = '魏老师'
    t2.tname = '王老师'
    t3.tname = '吕老师'
    t4.tname = '王老师'
    t5.tname = '赵老师'
    t1.tage = 40
    t2.tage = 32
    t3.tage = 35
    t4.tage = 33
    t5.tage = 47
    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(t4)
    db.session.add(t5)
    return '老师注册成功'


@app.route('/01')
def register_student():
    s1 = Student()
    s2 = Student()
    s3 = Student()
    s4 = Student()
    s5 = Student()
    s6 = Student()
    s7 = Student()
    s8 = Student()
    s1.sname = '秦健勇'
    s2.sname = '郝善伟'
    s3.sname = '胡锦飞'
    s4.sname = '王昆明'
    s5.sname = '张智'
    s6.sname = '张秀云'
    s7.sname = '朱承钦'
    s8.sname = '车姐'
    s1.sage = 24
    s2.sage = 22
    s3.sage = 22
    s4.sage = 32
    s5.sage = 30
    s6.sage = 28
    s7.sage = 26
    s8.sage = 32
    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)
    db.session.add(s4)
    db.session.add(s5)
    db.session.add(s6)
    db.session.add(s7)
    db.session.add(s8)
    return '学生注册成功'


@app.route('/01-parent')
def parents():
    p1 = Parents()
    p2 = Parents()
    p3 = Parents()
    p4 = Parents()
    p1.pname = '王妈妈'
    p1.page = 50
    p2.pname = '王爸爸'
    p2.page = 53
    p3.pname = '张妈妈'
    p3.page = 51
    p4.pname = '张爸爸'
    p4.page = 55
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    return 'ok'





@app.route('/02-rigister')
def student_teacher():
    students = Student.query.filter(Student.id.in_([2,3,4])).all()
    print(students)
    tea = Teacher.query.filter_by(id=1).first()
    for stu in students:
        tea.students.append(stu)
        db.session.add(tea)
    return 'ok'

@app.route('/02-parent')
def parent():
    p1 = Parents.query.filter_by(id=1).first()
    p2 = Parents.query.filter_by(id=2).first()
    p3 = Parents.query.filter_by(id=3).first()
    p4 = Parents.query.filter_by(id=4).first()
    s1 = Student.query.filter_by(id=4).first()
    s2 = Student.query.filter_by(id=5).first()
    s1.parents = [p1,p2]
    s2.parents = [p3,p4]
    db.session.add(s1)
    db.session.add(s2)
    return 'ok'





@app.route('/03-yanzheng')
def yanzheng():
    name = request.args.get('name')
    tname = Teacher.query.filter_by(tname=name).first()
    if not tname:
        return '不存在'

















if __name__ == '__main__':
    app.run(debug=True)