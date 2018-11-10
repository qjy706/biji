from flask import Flask,request,render_template,redirect,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/lianxi'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)


class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)
    def __repr__(self):
        return '<teacher:%r>' % self.tname




class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)

    teachers  = db.relationship('Teacher',lazy='dynamic',secondary='student_teacher',
                                backref=db.backref('students', lazy='dynamic')
                                )
    def __repr__(self):
        return '<student:%r>' % self.sname



student_teacher = db.Table(
    'student_teacher',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('Student.id',db.Integer,db.ForeignKey('Student.id')),
    db.Column('Teacher_id', db.Integer, db.ForeignKey('Teacher.id'))
)


db.create_all()

@app.route('/student')
def student():
    student = Student()
    student.sname = '黑皮'
    student.sage = 30

    db.session.add(student)
    return 'ok'


@app.route('/teacher')
def teacher():
    tea = Teacher()
    tea.tname = '吕老师'
    tea.tage = 35

    db.session.add(tea)
    return 'ok'


@app.route('/add')
def add():
    stu = Student.query.filter_by(id=1).first()
    print(stu)
    tea = Teacher.query.filter_by(id=1).first()
    tea2 = Teacher.query.filter_by(id=2).first()
    print(tea)
    stu.teachers.append(tea)
    stu.teachers.append(tea2)
    db.session.add(stu)
    return 'ok'



@app.route('/aaa')
def aaa():
    tea =Teacher.query.filter_by(id=1).first()
    m=tea.students.all()
    for x in m:
        print(x.sname)
    return 'x'






if __name__ == '__main__':
    app.run(debug=True)