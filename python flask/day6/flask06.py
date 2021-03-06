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
#
# db.init_app(app)



class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30),nullable=False)
    #增加关联属性和反向引用关系
    #关联属性　: 在course对象中　通过哪个属性能够得到对应的所有的teacher
    teachers = db.relationship('Teacher',backref='course',lazy='dynamic')
    #反向引用关系　: 在teacher对象中通过哪个属性能找到他对应的course
    #backref='course'是在teacher里面动态加进去的，隐藏的　运行的时候会在里面


    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return '<course:%r>' % self.cname


class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)
    #增加一列　: course_id ,外键列，要引用自主键表(course)的主键列(id)
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    #增加关联关系以及反向引用属性
    #是一个独立的对象　不是一个列表　
    wife = db.relationship('Wife',backref='teacher',uselist=False)

    courses = db.relationship('Student', secondary='student_teacher', lazy='dynamic',
                              #防止数据过大造成性能降低，关联和反向都设置一个懒惰
                              backref=db.backref('teacher', lazy='dynamic'))


    def __repr__(self):
        return '<Teacher:%r>' % self.tname



class Wife(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
    #增加一个列(外键)表示引用自Teacher表的主键
    teacher_id = db.Column(db.Integer,db.ForeignKey('Teacher.id'))


    def __init__(self,wname,wage):
        self.wname = wname
        self.wage = wage

    def __repr__(self):
        return '<Wife:%r>' % self.wname


#多对多

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)


    # 增加关联属性　以及反向引用　 随便哪张多表都可以
    courses = db.relationship('Course',secondary='student_course',lazy='dynamic',
                              backref=db.backref('students',lazy='dynamic'))

    def __repr__(self):
        return '<student:%r>'%self.sname



#创建多对多的第三张关联表，不需要对应的实体类，

student_course = db.Table(
    # 指定关联表的表名
    # 指定关联表的主键
    # 指定外键，关联一张多表的主键
    # 指定外键，关联另外一张的主键
    #分别关联多表的主键
    'student_course',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    )


student_teacher = db.Table(
    'student_teacher',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('Teacher_id', db.Integer, db.ForeignKey('Teacher.id')))



@app.route('/01-addcourse')
def add_course():
    course1 = Course('python基础')

    db.session.add(course1)
    course2 = Course('python高级')

    db.session.add(course2)
    course3 = Course('python数据库')

    db.session.add(course3)
    return '帅'



@app.route('/02-register-teacher')
def register_teacher():
    teacher = Teacher()
    teacher.tname= '魏老师'
    teacher.tage = 28
    #通过关联属性进行赋值　 在多表中
    #现货去一个course 对象
    course = Course.query.filter_by(id=1).first()
    #在将course对象赋值给teacher 其实是对象　 course属性需要赋值　
    teacher.course  = course
    #保存到数据路
    db.session.add(teacher)

    #通过外键id进行赋值　
    # teacher1.tname= '王老师'
    # teacher1.tage = 30
    #
    # teacher1.course_id = 1
    # db.session.add(teacher1)
    return '帅'

@app.route('/03-query-teacher')
def query_teacher():
    #通过course查找对应的所有的老师
    #查找course_id为1的course对象 first返回的是一个对象　
    course = Course.query.filter_by(id=1).first()
    print('课程名称'+course.cname)
    #查找course对应的所有的teacher们 　all()返回的是一个列表　需要遍历
    c = course.teachers
    print(c)
    teachers = course.teachers.all()
    for tea in teachers:
        print('教师姓名'+tea.tname)



    #通过teacher的course属性查找对应的course
    teacher = Teacher.query.filter_by(id=1).first()
    print('教师姓名'+teacher.tname)

    course1 = teacher.course
    print('教授课程'+course1.cname)
    return 'Query OK'

@app.route('/04-regTeacher',methods=['GET','POST'])
def regTeacher():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('04-regTeacher.html',courses=courses)
    else:
        tname = request.form.get('tname')
        tage = request.form.get('tage')
        course_id = request.form.get('course')
        #将三个数据构建成Teacher对象，再保存回数据库
        teacher = Teacher()
        teacher.tname = tname
        teacher.tage = tage
        teacher.course_id = course_id
        db.session.add(teacher)
        return redirect('/05-showTea')


@app.route('/05-showTea',methods=['POST'])
def showTea():
    teachers=Teacher.query.all()
    return render_template('05-showTea.html',teachers=teachers)



@app.route('/06-regWife')
def regWife():
    # wife = Wife('王夫人',18)
    # wife.teacher_id = 1
    # db.session.add(wife)
#通过对象赋值
    wife=Wife('魏夫人',15)
    teacher= Teacher.query.filter_by(tname='魏老师').first()
    wife.teacher = teacher
    db.session.add(wife)
    return '帅'

@app.route('/07-querywife')
def querywife():
    #通过teacher赵wife
    teacher = Teacher.query.filter_by(id=1).first()
    wife=teacher.wife

    #通过wife 找teacher
    wife = Wife.query.filter_by(id=2).first()
    teacher = wife.teacher
    return teacher.tname,wife.wname


@app.route('/08-asc')
def add_student_course():
    #获取id为1的学生信息 就给id为１的学员添加课程信息　
    student = Student.query.filter_by(id=1).first()
    #获取id为1的课程信息
    course = Course.query.filter_by(id=1).first()
    #将student与course关联到一起　一对多是一个列表
    student.courses.append(course)
    db.session.add(student)
    return 'Add course OK'



@app.route('/09=get')
def get():
    student = Student.query.filter_by(id=1).first()
    # 设置时候因为是lazy，所以要用到取值函数才能取值
    courses = student.courses.all()
    print(courses)
    return 'query ok'


@app.route('/010-refister-student',methods=['GET','POST'])
def show():
    if request.method == 'GET':
        students = db.session.query(Student).all()
        teachers =  db.session.query(Teacher).all()
        print(teachers)
        return render_template('010-refister-student.html',students=students,teachers=teachers)
    else:
        sname = request.form.get('xueyuan')
        student = Student.query.filter_by(sname=sname).first()
        print(student)
        # getlist 以列表的形式获取提交的所有值
        teachername = request.form.getlist('teacher')
        print(teachername)
        # 返回是一个列表
        teacher = Teacher.query.filter(Teacher.tname.in_(teachername)).all()
        print(teacher)
        for tea in teacher:
            #老师添加学生
            tea.courses.append(student)
            db.session.add(tea)
        return 'ok'


@app.route('/011-show')
def query11():
    teacher = Teacher.query.all()
    return render_template('011-query.html',teacher = teacher)


db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
