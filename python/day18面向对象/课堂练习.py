# class keybroad:
#     def __init__(self,name,qqq):
#         self.name=name
#         self.price=qqq
#         print(self.name,self.price)




# a=keybroad('hp',122)

#类变量

class Human:
    total_count=0# 类变量　用来记录Human人数
    pass

print(Human.total_count)# 访问类的变量　
h1=Human()l.llllllllllllk.........................
print(h1.total_count)#借助于此类的实例访问类变量

h1.total_count=10000# 为实例添加实例变量

print(h1.total_count)
# 会优先寻找对象自己属性的变量，没有回去找类的变量
print(Human.total_count)#用实例访问类的变量是改变不了类变量的

h1.__class__.total_count += 1#可以用实例h1的类的属性来改变类的属性
# 等同于Human.total_count += 1
print(Human.total_count)

Human.total_count += 1
print(Human.total_count)
print(dir(Human))



# class Human:
#     total_count = 0
#     def __init__(self,n):
#         self.name=n
#         self.__class__.total_count += 1
#         # 类的变量加１ 
#         print(n,'对象被创建')
#     def __del__(self):
#         print(self.name,'对象被销毁')
#         self.__class__.total_count -= 1

# L=[]
# L.append(Human('张飞'))
# L.append(Human('关羽'))
# print('当前人物个数是',Human.total_count)
# del L[1]
# print('当前人物个数是',Human.total_count)
# 张飞 对象被创建
# 关羽 对象被创建
# 当前人物个数是 2
# 关羽 对象被销毁
# 当前人物个数是 1
# 张飞 对象被销毁


#类的　__slots__列表　
# class Human:
#     __slots__=['name','age']#实例属性定死，只有name,age两种
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def info(self):
#         print(self.name,'今年',self.age,'岁')

# h1=Human('小张',8)
# h1.info()# 小张今年８岁
# h1.Age=9#属性名不同　添加了一个新的属性　
# h1.info()# 小张今年８岁
#如果不希望再添加新的属性　就需要添加slots列表
# 小张 今年 8 岁
# Traceback (most recent call last):
#   File "课堂练习.py", line 74, in <module>
#     h1.Age=9#属性名不同　添加了一个新的属性　
# AttributeError: 'Human' object has no attribute 'Age'


# class Human:
#     many=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(self.name,self.age)
# h1=Human('qqq',99)
# print(h1.many)
# h1.__class__.many=5
# print(h1.many)

类方法
class A:
    v = 0# 类的属性　

    @classmethod# 用于描述类的方法
    def get_v(cls,name=''):
        cls.v+=5  
        # 类变量赋值
        cls.name=name#新创建一个类的属性
        return cls.v,cls.name# 用cls访问类变量V　
print('A.v=',A.get_v('qqq'))#调用类方法得到类变量的值
# 跟实例方法很像，实例方法是　实例.方法函数（）　
# 类方法是　类.类方法() 
a=A() 
print('A.v=',a.get_v())# 此类的实例也可以调用该类方法
print(A.v)
a是个对象　，装饰器函数classmethod会自动把对象转换成a.__class__
保证第一个参数永远是对象的类




#类方法不能访问此类创建的对象的实例属性　
# class A:
#     v = 0
#     @classmethod
#     def set_v(cls,a):
#         '''能否访问a.color属性'''
#         cls.v=a
#         print(cls.color)

# a=A()
# a.color='#ff0000'
# a.set_v(100)


#静态方法　@staticmethod 
# class A:
#     @staticmethod
#     def myadd(a,b):
#         return a+b
# print(A.myadd(100,200))
# a=A()
# print(a.myadd(300,400)
#跟普通函数一样，只是在类里面　作为一个算法用　
# 不能访问类的变量　和实例的变量　实质就是函数　
#用在之定义在这个类里面的，不给其他人用才可以　


# 用类来描述一个一个学生信息（可以修改之前写的student类)
# class Student:
#学生信息有姓名，　年龄，　成绩
# 讲学生对象存于列表中　　可以任意添加和删除学生　
# 打印出学生的个数　　平均年龄　　　平均成绩　
# class Student:
#     L=[]
#     def __init__(self,name,age,score=0):#初始化对象
#         self.name=name#实例属性赋值
#         self.age=age
#         self.score=score

#     @classmethod#类的装饰器
#     def add_student(cls):
#         cls.L.append(Student('小张',20,100))
#类的属性Ｌ添加一个对象小张　20　100　
#         cls.L.append(Student('小李',30,80))
#         cls.L.append(Student('小王',19,60))

#     @classmethod
#     def get_student_count(cls):
#         return len(cls.L)
#     
#     @classmethod
#     def get_avg_score(cls):
#         return sum(map(lambda x: x.score,cls.L))/len(cls.L)
#     @classmethod
#     def get_avg_age(cls):
#         return sum(map(lambda x: x.age,cls.L))/len(cls.L)


# Student.add_student()

# print(Student.get_avg_score())


单继承　

class Human:
    def say(self,what):
        print('说：',what)

    def walk(self,distance):
        print('走了',distance,'公里')

class Student(Human):#当前学生类继承自Human
# Human派生了学生类　　Human就是父类　
    # def say(self,what):
    #     print('说：',what)
    # pass # 这时候跟Human没啥区别　派生了一个新类　但功能跟huamn一样

    # def walk(self,distance):
    #     print('走了',distance,'公里')
    def study(self,subject):
        print('正在学习',subject)

h1=Human()
h1.say('今天天气真好')
h1.walk(5)

s1=Student()
s1.walk(4)
s1.say('感觉有点累')
s1.study('python')


list 类里只有append 想末尾加一个元素的方法，但没有向列表头部
添加元素的方法　
是想能否列表在不改变原有功能的基础上添加一个insert_head(x)方法
此方法能在列表的前部添加元素　
class MyList(list):#好比老虎是猫也是生物　mylist是类也是列表
    def insert_head(self,x):
        self.insert(0,x)
        return self 
        # self[0:0]=[x]
        # retuen self

myl=MyList(range(3,6))
print(myl)
# print(myl.insert_head(13))




#覆盖

# class A:
#     def work(self):
#         print('A.work被调用')

# class B(A):
#     '''B类继承A类'''
#     def work(self):
#         print('b.work被调用')
# # 一旦子类有跟父类同名的方法，方法的调用是子类的调用　是一种覆盖版本
# b=B()
# b.work()#A是Ｂ的父类　先找ｂ再找Ａ　　B.work(b)
# A.work(b)# 子类里面的对象调用父类的方法　但python不建议这样，可以用super
# # a=A()
# a.work()

# b.work被调用
# A.work被调用

# A.work被调用
# A.work被调用



super 函数
super 函数


class A:
    def work(self):
        print('A.work被调用')

class B(A):
    '''B类继承A类'''
    def work(self):
        print('b.work被调用')
# 一旦子类有跟父类同名的方法，方法的调用是子类的调用　是一种覆盖版本
　　　　def super_work(self):
        self.work()
        super(B,self).work()
        super(self.__class__,self).work()
        super().work()# 当super没有参数的时候会找到调用他的类
# 和对象　　但必须在方法内部（示例方法内部调用）
b=B()
b.work()#A是Ｂ的父类　先找ｂ再找Ａ　　B.work(b)
super(B,b).work()#超类　是　先找Ｂ的超类Ａ　　把b当成Ａ的对象
把子类对象看成父类对象


有覆盖才有超类
#显示调用基类的初始化方法　
class Human:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print('Human初始化方法被调用')
    def infos(self):
        print('姓名',self.name)
        print('年龄',self.age)

class Student(Human):#不大括号里面默认是objcet
    def __init__(self,n,a,s=0):#形成了覆盖　子类有父类相同的方法名
        super(Student,self).__init__(n,a)#Human的初始化方法,无参也可以
        #super().__init__(n,a)
#self已被看成父类的对象，调用父类的初始化方法　__init__(n,a)
#像__init__初始化方法，　Human('qqq',n,a)自动初始化==Human.__init__('qqq',n,a)
        self.score=s
        print('Student的初始化方法被调用')
    def infos(self):
        super(Student,self).infos()
#super函数把Student的父类函数找到，把self当作父类的实例，调用父类的方法infos()
        print('成绩',self.score)

s1=Student('张飞',15,80)
s1.infos()