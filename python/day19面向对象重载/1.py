# 用于类的函数

# class A:
#     pass 

# class B(A):
#     pass 

# class C(B):
#     pass 

# issubclass(C,B)
# #C类是不是Ｂ的子类　True
# issubclass(B,A)
# # True 
# issubclass(A,C)
# #False 


# issubclass(bool,int)
# # True 

# issubclass(int,object)
# #True

#上周作业

# class Bicycle:
#     def run(self,km):
#         print('自行车骑行',km,'公里')

# class EBicycle(Bicycle):
#     def __init__(self,vol):
#         self.volume=vol

#     def fill_charge(self,vol):


#     def run(self,km):
#         e_km=min(km,self.volume*10)
#         if e_km > 0:
#             self.volume -= e_km / 10
#             print('电动骑行%dkm,还剩下%.1f度电' % (e_km.self.volume))
#         if km > e_km:
#             a=km-e_km
#             super(self.__class__,self).run(a)
#             super(EBicycle,self).run(a)
#             



# 私有属性和方法
class A:
    def __init__(self):
        self.__p1=100
        # self.__p2__=200
#__p1为私有属性 只有开头双下划线,特殊的命名方式
    def show_info(self):
        print(self.__p1)#此对象的实例方法可以访问和修改私有属性
        self.__m()#用自己的方法调用自己的私有方法没有问题
#私有方法只给自己用　私有属性也是只给自己用　
    def __m(self):
        print('A类对象的__m方法被调用')#__m相当于Ａ的类变量，绑定的是方法

a=A()
# print(a.__p1)#私有属性不允许访问
print(a._A__p1)#这样又可以了　是一个障眼法　实例加一个下划线加一个类名加隐藏属性就可以访问了
#只能在内部进行访问
a.show_info()
# 对象的私有属性要通过对象的方法来进行访问
# 私有属性要通过实例方法来调用和修改实例属性
# a.__m()#也是无法调用的



#多态　polymorphic 

class Shape:
    def draw(self):
        print('Shape的draw()被调用')

class Point(Shape):
    def draw(self):
        print('正在画一个点')

class Circle(Point):
    def draw(self):
        print('正在画一个圆')

def my_draw(s):
    s.draw()#此处调用哪种方法

s1=Circle()
s2=Point()
my_draw(s1)
my_draw(s2)

#多继承　multiple inheritance 
# class Car:
#     def run(self,speed):
#         print('汽车以',speed,'公里每小时速度行驶')
# class Plane:
#     '''飞机类'''
#     def fly(self,height):
#         print('飞机以海拔',height,'高度飞行')

# class PlaneCar(Car,Plane):
#     '''同时继承汽车和飞机'''


# p=PlaneCar()
# p.fly(10000)
# p.run(300)
# 飞机以海拔 10000 高度飞行
# 汽车以 300 公里每小时速度行驶

#多继承父类标识符冲突　
# class ab(A,B)
#以Ａ的方法为准　

# class A:
#     def m(self):
#         print('A.m被调用')
# class B:
#     def m(self):
#         print('B.m被调用')
# class AB(A,B):
#     pass 
# ab=AB()
# ab.m


# AB.__mro__

#多继承MRO问题
# class A:
#     def go(self):
#         print('A')
# class B(A):
#     def go(self):
#         print('B')
#         super().go()
# class C(A):
#     def go(self):
#         print('C')
#         super().go()

# class D(B,C):
#     def go(self):
#         print('D')
#         super().go()
# d=D()
# print(D.__mro__)
# d.go()


# D
# B
# C
# A
# <class '__main__.D'>
# <class '__main__.B'>
# <class '__main__.C'>
# <class '__main__.A'>
# <class 'object'>

# 写一个农民类Peasant 有方法：
# def farm(self,plant):
#     ...

# 写一个工人类 Worker 
#   方法　　
#   def work(self,that):
# 创建一个农民工为MigrantWorker 让此类的对象拥有上面两个
# 类的全部方法　
# person=MigrantWorker()
# person.farm('水稻')#正在种植水稻
# person.work('汽车')# 正在制造汽车
# 查看个各类的__mro__属性　


# 函数重写　　overwrite  
# s='i am teacher'
# L=[1,2,3,4]
# print(str(s))
# print(repr(s))
# print(repr(L))
# print(eval(repr(s)))
# i am teacher
# 'i am teacher'   
# repr多了一个引号　转成了python可以识别的表达式　
# str转换成了内容人可以看　


# 对象转字符串函数的重写方法　

# repr()函数重写方法：
# def __repr__(self):
#     return 字符串


# str()函数重写方法：
# def __str__(self):
#     return 字符串


# str(obj)函数调用方法说明
# 1. str(obj)函数先查找obj.__str__(方法)
#    调用此方法并返回结果　

# ２．如何obj.__str__()
# 方法不存在，则调用obj.__repr__方法并返回结果

# ３. 如果obj.__repr__
# 方法不存在，则调用object类的__repr__实例方法显示
# <__main__.xxx object at 0xXXXXXXX>格式字符串
# 内存地址加名字　覆盖思想　有一个object超类　　

# class MyNumber:
#     def __init__(self,val):
#         self.data=val 
#     def __str__(self):
#         return '自定义数字:%d' % self.data
#     def __repr__(self):
#         '''从方法返回来的字符串一定是能表示self对象的表达式字符串'''
#         return 'MyNumber(%d)' % self.data
# n1=MyNumber(100)
# print('str(n1)=',str(n1))
# print('repr(n1)',repr(n1))
# print(n1)#相当于str(n1)
# n2=MyNumber(200)
# print('str(n2)=',str(n2))
# print('str(n2)=',n2.__str__())
# print(n2)#在print内部会将n2用str（x)转为字符串再写到sys.stdout(标准输出文件)
# print('repr(n1)=',repr(n1))
# 有一个父类object　里面也有相同的方法　
# str(n1)  == n1.__str__ MyNumber里面有__str__　覆盖了父类__str__



# class MyList():
#     '''这是一个自定义的列表类型，
#     此类型的对象用data属性绑定的列表来存储数据'''
#     def __init__(self,iterable=()):
#         self.data=[x for x in iterable]


#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     # def __str__(self):
#     #     return 'MyList(%s)' % self.data

#     def __len__(self):
#         return len(self.data)
#     # def __abs__(self):
#     #     L=[]
#     #     for x in self.data:
#     #         L.append(abs(x))
#     #     return 'MyList(%s)' % L



# myl= MyList([1,-2,3,-4])
# print(myl)#里面没有重写函数的话返回的是一个地址
# print(myl.__str__())
# print(len(myl))#其实等于myl.__len__() 但是类里面没有这个函数
#只能去超类object寻找，但返回的是一个地址　
#只能在类中创建一个函数　，这就叫函数重写
# print(myl.__len__())
# print(abs(myl))


# 数值转换函数的重写
# class MyNumber:
#     def __init__(self,val):
#         self.data=val 
# #     def __repr__(self):
# # #         '''从方法返回来的字符串一定是能表示self对象的表达式字符串'''
# #         return 'MyNumber(%d)' % self.data
#     def __int__(self):
#         return int(self.data)#如果是字符串里面的数字　再加一个int
#     def __float__(self):
#         return float(self.data)

# n1=MyNumber(100)
# print(int(n1))#MyNumber类中如果没有__int__函数　会去找超类的

# c=complex(n1)
# print(c)#当没有n1.__complex__()时会调用n1.__float__()


#布尔测试函数的重写
# 格式　
# 　　def __bool__(self):
#        ...

# 作用　
# 　　　　用于bool(obj)函数取值
# 　　　　用于if语句真值表达式中　
# 　　　　用于while语句的真值表达式中

# 说明：
# 　　　　１，当自定义类内有__bool__(self)方法时，此方法的返回作为bool（ｘ）
# 的返回值
# 　　　　２，当不存在__bool__(self)方法时，返回__len__(self)
# 方法的返回值是否为非零来测试布尔值
# 　　　　３，当不存在__len__(self)方法时，则直接返回True
# 　　　　


# class MyList():
#     '''这是一个自定义的列表类型，
#     此类型的对象用data属性绑定的列表来存储数据'''
#     def __init__(self,iterable=()):
#         self.data=[x for x in iterable]


#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     # def __str__(self):
#     #     return 'MyList(%s)' % self.data

#     def __len__(self):
#         return len(self.data)

#     def __bool__(self):
#         print('__bool__方法被调用')
#         for x in self.data:
#             if x:
#                 return True
#             return False
#             return any(self.data)

# myl=MyList([False,0,0.0])
# print(bool(myl))
# if myl:
#     print(myl,'的布尔值为True')
# else:
#     print(myl,'的布尔值为False')



# class Dog:
#     pass 
# d=Dog()
# setattr(d,'color','白色')# 等同于d.color='白色'
# #setattr 添加修改属性

# hasattr(d,'color')
# True 
# #判断　

# getattr(d,'color')
# '白色'
# #如果没有该属性　，报错　要用到try语句 except 赋值

# delattr(d,'color')#del d.color


# 迭代器（高级）　
class MyList():
    '''这是一个自定义的列表类型，
    此类型的对象用data属性绑定的列表来存储数据'''
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]


    def __repr__(self):
        return 'MyList(%s)' % self.data
    def __iter__(self):
        print('__iter__被调用')
        return MyListIterator(self.data)
        #return iter(self.data)


class MyListIterator:
    def __init__(self,lst):
        self.data_lst=lst
        self.cur_index=0

    def __next__(self):
        print('__next__方法被调用')
        if self.cur_index >= len(self.data_lst):
            raise StopIteration

        r=self.data_lst[self.cur_index]
        self.cur_index += 1
        return r
myl=MyList([2,3,5,7])
it=iter(myl)
#it=myl.__iter__() 相当于重写
#这时候类里面没有__iter__(self)只能寻找超类，但返回的是一个地址　报错
# print(next(it))

for x in myl:
    print(x)



#练习　１实现学生信息管理系统的student类的封装，让出　Student实例方法
# 外的函数或其他方法都不能访问姓名，年龄，成绩等属性　

# ２，写一个实现迭代器协议的类　，让此类可以生成从ｂ开始的ｎ个素数
# class Prime:
#     def __init__(self,b,n):
#         ...
#     def __iter__(self):
#         ...
#     def __next__(self):

# class 666:
#     def prime(self):


# L=[x for x in Prime(10,4)]
# print(L) # L=[11,13,17,19]


# 3,写一个类　Fibonacci 实现迭代器协议，　此类的对象可以作为可迭代对象生成斐波那契书名

# 1,1,2,3,5,8,13..

# class Fibonacci:
#     def __init__(self,n):



# for x in Fibonacci(10):
#     print(x)

# ２，写一个实现迭代器协议的类　，让此类可以生成从ｂ开始的ｎ个素数
# class Prime:
#     def __init__(self,b,n):
#         ...
#     def __iter__(self):
#         ...
#     def __next__(self):

# class 666:
#     def prime(self):
# L=[x for x in Prime(10,4)]
# print(L) # L=[11,13,17,19]



# class qqq:

#     def __init__(self,a):
#         self.a=a
#     def isaprime(self):
#         if self.a < 2:
#             pass
#         for i in range(2,self.a):
#             if self.a % i == 0:
#                 return False
#             return self.a

# # L=qqq(10)
# # print(L.isaprime())
# class Prime:
#     def __init__(self,b,n,L=[],s=0):
#         self.b=b
#         self.walk=n
#         self.L=[]
#         self.s=0
#     def __iter__(self):
#         while self.s < self.walk:
#             if qqq(self.b):
#                 self.L.append(qqq(self.b).isaprime())
#                 self.s += 1
#                 self.b += 1
#             if self.s == self.walk:
#                 break
#         return iter(self.L)

    # def __next__(self):
    #     for x in self.L:
    #         if x == 'False':
    #             del self.L.remove(x)
    #     return self.L
      



# L=Prime(10,8)
# a=[x for x in iter(L)]
# print(a)












# 3,写一个类　Fibonacci 实现迭代器协议，　此类的对象可以作为可迭代对象生成斐波那契书名

# 1,1,2,3,5,8,13..

# class Fibonacci:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):


# f(0)=0 f(1)=1 f(n)=f(n-1)+f(n-2)









