# class dog:
#     '''创建一个Dog类,此类用于描述
#     一种小动物的行为和属性,dog是一个变量名绑定一个类'''
#     pass


# dog1=dog() 
# 一定会创建dog类的实例  构造函数
# print(id(dog1))
# #140011116083128
# dog2=dog()
# print(id(dog2))
# #dog2 就是实例变量(属性)
# 也是类里面的对象　　比如class car　　那么bmw=car
# bmw 就是一个车类里面的一辆车　用bmw变量绑定　代表　bmw车
# #140011092182912
# #id不同　地址不同　两个对象　

# 实例方法

# class dog:# （继承列表)
#     '''创建一个dog类,此类用于描述
#     一种小动物的行为和属性,dog是一个变量名绑定一个类'''
#     def eat(self,food):
#         '''此方法用来描述小狗吃东西'''
#         print('小狗正在吃',food)
#     def sleep(self,hour):
#         print('小狗睡了',hour,'小时')


# dog1=dog()
# # dog1 绑定这个类　
# dog1.eat('骨头')
# dog1.sleep(5)   #实例方法 
# eat sleep都是描述对象行为的方法
# self是dog1 是方法的调用者 , 调用了类绑定的对象的属性和行为（方法）
# 也就是描述类里面对象的方法
# 让此类对象都有相同的行为　比如小狗　就调用这个dog类对象的行为（里面的方法）　
# 列表就调用列表里面的方法　，append remove sort reverse pop count
# insert(index,obj)
# 同一个类的对象都有相同的行为　车都有四个轮子　list都有append

#这也是一个模块　里面包含了一个类　dog


# 示例属性
#此示例示意为对象添加实例变量（实例属性）及访问实例变量（实例属性）
# class Dog:
#     def eat(self,food):
#         print(self.color,'的',self.kinds,'正在吃',food) 
#         #谁调用了eat　谁就调用了self.color自身的属性
#         self.last_food=food# 类里面的对象谁调用了　谁就显示让一次吃的事物
#     def show_last_food(self):
#         print(self.color,'的',self.kinds,'上次吃的是',self.last_food)

# dog1=Dog()
# # 变量名dog1绑定一个Dog类的一条狗形成一个对象　
# dog1.kinds='京巴'# 添加实例属性　 也是一条赋值语句　赋值给对象的变量
# dog1.color='白色'# 添加
# dog1.color='黄色'# 修改实例属性的绑定关系


# dog2=Dog()# 变量名dog2绑定一个Dog类的一条狗形成一个对象　
# dog2.kinds='藏獒'
# dog1.color='棕色'
# print(dog1.color,'的',dog1.kinds)
# # print(dog2.color,'的',dog2.kinds)


# dog1.eat('骨头')
# dog1.show_last_food()

# # 定义一个　人　human　类　
# class Human:
#     def set_info(self,name,age,address='不详'):# 实例方法名
#         '''此方法用来给人对象添加姓名，年龄，家庭住址属性'''
#         self.name=name# 实例变量（属性）
#         self.age=age
#         self.address=address
#         #当动用方法时候，对象变成自己 .自己该怎么做 self.xxx
#         #语法：
#         #实例.属性名

#     def show_info(self):
#         '''此处显示此人的信息'''
#         print(self.xxx,'今年',self.age,'家庭地址',self.address)





# # 调用如下:
# h1=Human()  
# #创建了一个对象
# h1.set_info('车姐',20,'北京市东城区')
# # h2=Human()
# # h2.set_info('小李',10)
# h1.show_info()# 实例方法　　　实例.实例方法名（）
# # h2.show_info()




#初始化方法
# class car:
#     def __init__(self,c,b,m):
#         self.color=c
#         self.brand=b
#         self.model=m# 实例属性语句　进入面向对象内部　这时候是自己想干什么
#         #自己该怎么做

#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,'正在以',speed,'公里每小时行驶')
# BMW=car('棕色','宝马','M760i')# 绑定了车这个类里面的一个对象　用ＢＭＷ绑定
# BMW.run(120)#实例方法语句


# 练习，
# 写一个student类　此类创建的对象有三个属性，
# 姓名，　年龄　成绩　
# １）　用初始化方法为该类添加上述三个属性　
# ２）　添加set_score() 方法能为对象修改学生成绩　
# 3）　添加show_info()方法　打印学生信息　

# class Student():
#     def __init__(self,names,age,score=0):
#         self.names=names
#         self.age=age
#         self.score=score
#         # self.names,self.age ,self.score=names,age,score
#     def set_score(self,score):
#         if 0 <= score <= 100:
#             self.score=score

#     def show_info(self):
#         print('姓名',self.names,'年龄',self.age,'成绩',self.score)
# L=[]
# L.append(Student('小张',20,100))
# L.append(Student('小李',40,98))
# L.append(Student('小秦',19,80))
# L[2].set_score(99)
# for x in L:
#     x.show_info()




# one=Student('小张',20,98)
# one.set_score(30)
# one.show_info()


# 析构方法

# class car:
#     def __init__(self,info):# 初始化方法
#         self.info = info
#         print('汽车对象',info,'被创建')
#     def __del__(self):
#         print('汽车对象',self.info,'被销毁')

# c1=car('byd e6')
# # c1=None# 改变变量的绑定关系可以释放byd e6对象
# del c1 
# L=[]
# L.append(car('汽车1'))
# L.append(car('汽车2'))
# L.append(car('汽车3'))
# del L#这样释放列表也是可以释放对象
# input('请输入回车键继续执行程序')# 程序结束之后所有对象被释放
# print('程序退出')


# 面向对象的综合示例：
# 有两个人
# 属性　　
# 　１　姓名：张三　，年龄　３５岁　
# 　２　姓名：李四　，年龄　８岁　

# 行为：
# １　教别人学东西　teach 
# 2 工作赚钱　work
# 3　借钱　borrow

# 事情：
# 张三　教　李四学　python
# 李四　教　张三　学　王者荣耀　
# 张三　上班赚了　１０００元　
# 李四　向　张三　借了２００元钱　
# ３５岁的张三有钱　８００元，它学会的技能:王者荣耀　，
# ８岁的　李四　有钱　２００元　，他学会的技能：　python

# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def teach(self,name):
#         if self.name == '张三':
#             print(self.name,'教',name,'python')
#         else:
#             print(self.name,'教',name,'王者荣耀')

#     def work(self,money):
#         if self.name is '张三':
#             print(self.name,'上班赚了',money)
#         else:
#             print('不成立')

#     def borrow(self,name,money):
#         if self.name is '李四':
#             print(self.name,'向',name,'借了',money)
#         else:
#             print('张三不缺钱')
#     def fin(self,money,skill):
#         if self.name is '张三':
#             print(self.age,'的',self.name,'有钱',money,'学会的技能',skill)
#         else:
#             print(self.age,'的',self.name,'借钱',money,'学会的技能',skill)




# man1=Human('张三',35)
# man1.teach('李四')
# man1.work(1000)
# man1.fin(800,'王者荣耀')

# class Human:# 类　
#     def __init__(self,n,a):　# 初始化方法(实例方法)
#         self.name=n# 实例属性语句(用来保存用户自己的数据)
#         self.age=a
#         self.money=0#提前添加一个钱数（实例属性）
#         self.skill=[]#添加技能（这个也是添加了一个属性)
#     def teach(self,other,skill):
#         print(self.name,'教',other.name,'学',skill)
#         other.skill.append(skill)#other增加技能
#     def work(self,m):
#         print(self.name,'上班赚了',m,'元钱')
#         self.money += m
#     def borrow(self,other,m):
#         if borrow.money > m:
#             print(self.name,'向',other.name,'借了',m,'元钱')
#             other.money -= m
#             self.money += m
#         else:
#             print('借钱失败')
#     def show_info(self):
#         print(self.age,'岁的',self.name,'有钱',self.money,'元','他学会的技能',self.skill,)


# zhang3=Human('张三',35)
# li4=Human('李四',8)
# zhang3.teach(li4,'python')
# li4.teach(zhang3,'王者荣耀')
# zhang3.work(1000)
# li4.borrow(zhang3,200)
# zhang3.show_info()
# li4.show_info()

# 事情：
# 张三　教　李四学　python
# 李四　教　张三　学　王者荣耀　
# 张三　上班赚了　１０００元　
# 李四　向　张三　借了２００元钱　
# ３５岁的张三有钱　８００元，它学会的技能:王者荣耀　，
# ８岁的　李四　有钱　２００元　，他学会的技能：　python

# 昨日作业
# L=[]
# while True:
#     n=int(input('请输入大于零的整数'))
#     if n < 0:
#         break
#     L.append(n)
# print(L)
# try:
#     f=open('numbers.txt','w')
#     for n in L:
#         n=str(n)
#         f.write(n+'\n')
#     f.close()
# except:
#     print('打开失败')


# def mycopy(src_filename,dst_filename):#目标文件名
#     try:
#         fr=open(src_filename,'rb')
#         try:
#             try:
#                 fw=open(dst_filename,'wb')
#                 try:
#                     while True:
#                         b=fe.read(4096)
#                         if not b:
#                             break
#                         fw.write(b)
#                 finally:
#                     fw.close()
#             except OSError:
#                 print('打开目录文件失败')
#                 fr.close()
#         finally:
#             fr.close()
#     except OSError:
#         print('打开源文件失败')

# src=input('请输入源文件名字')
# dst=input('请输入目标文件名字')


# 1看懂面向对象示例　
# ２　学生信息管理程序，原来由字典保存每个信息，　现改为用对象来保存学生信息
# 要求讲student类来描述　将student类写在独立的模块：student.py中　；。’





# class qjy:
#     def __init__(self,name,age,money=0):
#         self.name=name
#         self.age=age
#         self.money=money
#         print(self.name,self.age,self.money)
#     def chifan(self,other):
#         print(self.name,'跟',other.name,'一起吃饭')# other=dyn other.name  == dyn.name
#         # dyn是绑定一个对象的变量　，　这个对象的属性是　丁　23　10000 　里面的变量已经被赋值　
#         # 实参dyn 传参到　other 　那么other.name就是dyn.name dyn只是对象的一种表达方式　
#         #dyn之前有过赋值　chifan()　好比　秦建勇是自己　self 　丁是other  other.name是实例属性　
#         # 也就是dyn的属性　，也就是　dyn.name


# qqq=qjy('秦建勇',24,2000)
# dyn=qjy('丁',23,10000)# 用dyn绑定的一个对象　并用初始化方法赋值属性
# qqq.chifan(dyn)
# dyn.chifan(qqq)


# class Human:
#     @staticmethod
#     def qqq(a,b):
#         return a+b
# a=Human()
# a.qqq(1,2)
# print(a.qqq(1,2))
# print(Human.qqq(300,500))


# class Human:
#     __slots__=['high','age','kg']
#     count=0
#     def __init__(self,h,a,kg=0):
#         self.high=h
#         self.age=a
#         self.kg=kg
#         print('信息录入成功')

#     @classmethod
#     def renshu(cls,a):
#         cls.count += 1
#         a.__class__.count += 1
#         return a.__class__.count

# qqq=Human(183,24,90)
# Human.renshu(qqq)
# print(Human.renshu(qqq))
# 练习：
#    用类来描述一个学生的信息，(可以修改之前写的Student类)
#     class Stdent:
#         ...此处自己实现
#     学生信息有:
#         姓名，年龄，成绩
#     将这些学生对象存于列表中，可以任意添加和删除学生
#       1) 打印出学生的个数
#       2) 打印出学生的平均成绩
#       3) 打印出学生的平均年龄
#       （建议用类内的列表来存储学生的信息)


# class Student:
#     L=[]
#     __slots__=['name','age','score']
#     def __init__(self,n,a,s=0):
#         self.name=n
#         self.age=a
#         self.score=s

#     @classmethod
#     def get_info(cls):
#         cls.L.append(Student("小张", 20, 100))
#         cls.L.append(Student("小李", 18, 80))
#         cls.L.append(Student("小赵", 19, 90))
#         print(cls.L)
# #Human的属性Ｌ添加实例的初始化属性
#     @classmethod
#     def print_ingo(cls):
#         return len(cls.L)

#     @classmethod
#     def print_avg_s(cls):
#         return sum(map(lambda obj: obj.score, cls.L)) / len(cls.L)

#     @classmethod
#     def print_avg_a(cls):
#         return sum(map(lambda obj: obj.age, cls.L)) / len(cls.L)

#     @classmethod
#     def del_student(cls):
#         del cls.L[0]


# Student.get_info()

# print('学生个数有',Student.print_ingo())
# print('学生平均成绩',Student.print_avg_s())
# print('学生平均年龄',Student.print_avg_a())
# Student.del_student()
# print('学生个数有',Student.print_ingo())
# print('学生平均成绩',Student.print_avg_s())
# print('学生平均年龄',Student.print_avg_a())




# class A:
#     def work(self):
#         print("A.work 被调用")

# class B(A):
#     '''B类继承自A类'''
#     def work(self):
#         print("B.work被调用!!!")

#     def super_work(self):
#         # 调用B类自己的方work方法怎么调用
#         self.work()
#         # 调用父类的work怎么调用
#         super(B, self).work()
#         super().work()  # 此种调用方式只能在实例方式内调用


# b = B()
# # b.work()  # B.work被调用!!!
# # super(B, b).work()  # A.work 被调用
# b.super_work()
# # super().work()  # 出错
# B.work被调用!!!
# A.work 被调用
# A.work 被调用


# class Human:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#         print('被调用')
#     def print_info(self):
#         print('姓名',self.name,'年龄',self.age)


# class Student(Human):#继承Human
#     def __init__(self,n,a,s=0):
#         super(Student,self).__init__(n,a)
#         #当前类的基类的方法被当前基类的对象调用
#         #这样可以无线添加属性
#         self.score=s
#     def infos(self):
#         super(Student,self).print_info()  # 显式调用父类的方法
#         print('成绩:', self.score)

# s1=Student('张飞',24,99)
# s1.infos()

# class Bicycle:
#     def run(self,km):
#         print('脚蹬骑行了',km,'公里')

# class EBicycle(Bicycle):

#     def __init__(self,v):
#         self.vol=v
#         print('新买的电动车里还有',self.vol,'度电')

#     def run(self, km):
#         a=0.1*km
#         if self.vol < a:
#             k=km-self.vol*10
#             print('电动骑行了',self.vol*10,'KM','还剩下',0,'度电')
#             self.vol=0
#             super(EBicycle,self).run(k)
#         else:
#             self.vol -= 0.1*km
#             print('骑行了',km,'公里','还剩下',self.vol,'电')

#     def fill_charge(self,v):
#         self.vol += v
#         print('充电',v,'度')
#         print('现在电量',self.vol,'度')



# b1=EBicycle(5)
# b1.run(10)
# b1.run(100)
# b1.fill_charge(10)
# b1.run(50)


# def sushu(x):
#     if x < 2:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True
# L=list(filter(sushu,range(101)))
# print(sum(L))