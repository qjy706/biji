# 　with语句

# try:
#     with open('xxx.txt') as f:#f=open('xxx.txt')
# #open是唯一能用with语句的
# #with　表达式１［as 变量1］,表达式２［as 变量２],..:
#         for l in f:
#             x=int('aaa')#当进入异常流程时，打开的文件也能被关闭
#             print(l)
# #当用with打开的时候不需要关闭文件 文件流自动判断是否关闭
# except OSError:
#     print('打开文件失败')



    # 资源管理器　

# class A:
#     '''此类的对象可以用于with语句进行管理'''
#     def __enter__(self):#进入with的执行环境
#         print('此方法是在with语句内被执行')
#         return self 
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         '''exc_type用来绑定错误类型,当没有异常发生时，绑定None
#         　　　exc_val　用来绑定错误对象，当没有发生异常时绑定None
#         　　　exc_tb  用来绑定TraceBack对象，当没有异常时绑定None'''
#         if exc_type is None:
#             print('您已离开with语句,离开时没有发生任何异常')
#         else:
#             print('您已离开with语句')
#             print('错误类型是',exc_type)
#             print('错误对象是',exc_val)
#             print('TraceBack',exc_tb)


# with A() as a:
#     print('这是with语句内部的输出')
#     int(input('请输入整数'))#即使异常　也会关闭,也就是必须要做的事情可以放在exit里面
#     #A不是资源管理器　

# print('程序正常结束')
# # 当用with打开文件里面实际是文件流里面的enter exit
# #此方法是在with语句内被执行
# # 这是with语句内部的输出
# # 您已离开with语句
# # 程序正常结束


# 运算符重载
# 算数运算符的重载

# class MyNumber:
#     def __init__(self,v):
#         self.data=v

#     def __repr__(self):
#         return 'MyNumber(%d)' % self.data

#     # def add(self,other):
#     def __add__(self,other):
#         v=self.data+other.data
#         return MyNumber(v)

#     def __sub__(self,other):
#         v=self.data-other.data
#         return MyNumber(v)

#     def __mul__(self,other):
#         v=self.data*other.data
#         return v

#     def __truediv__(self,other):
#         v=self.data/other.data
#         return v

#     def __floordiv__(self,other):
#         v=self.data//other.data
#         return v
#     def __mod__(self,other):
#         v=self.data%other.data
#         return v
#     def __pow__(self,other):
#         v=self.data**other.data
#         return v
#     def qqq(self,other):
#         v=self.data + other.data
#         return v



# n1=MyNumber(100)

# n2=MyNumber(200)
# # n3=n1.add(n2)
# n3=n1+n2 #等于n3=n1.__add__(n2)  调用def __add__(self,other):  
# # n3=n1+n2#这样子不行
# print(n3)
# n3=n1-n2
# print(n3)
# n3=n1*n2
# print(n3)
# n3=n1/n2
# print(n3)
# n3=n1//n2
# print(n3)
# n3=n1%n2
# print(n3)
# n3=n1**n2
# print(n3)
# n3=n1.qqq(n2)
# print(n3)




# 实现两个自定义列表的相加　
# class MyList:
#     def __init__(self,iterable=()):
#         self.data=list(iterable)


#     def __add__(self,other):
#         print('__add__被调用')
#         v=self.data+other.data
#         return MyList(v)

#     def __mul__(self,other):
#         print('__mul__被调用')

#         v=self.data*other
#         return MyList(v)

#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     def __rmul__(self,lhs):
#         print('__rmul__被调用')
#         return MyList(self.data*lhs)

#     def __iadd__(self,rhs):
#         print('__iadd__方法被调')
#         self.data+=rhs.data
#         return self






# L1=MyList([1,2,3])
# print(id(L1))
# L2=MyList([4,5,6])

# # L3=L1+L2
# # print(L3)

# # L4=L2+L1
# # print(L4)

# L3=3*L1
# print(L3)

# L1+=L2# L1=L1.__add__(L2)创建了一个新的对象
# print(id(L1))
# print(L1)
# 139982725123040
# __iadd__方法被调
# 139982725123040
# MyList([1, 2, 3, 4, 5, 6]) __iadd__ 等于没有创建一个新的对象　id并没有变化

# L2 *= 3#L2= L2.__mul__(3)
# print(L2)

# 试想
# L5=L1*3
# print(L5)



# 一元运算符的重载　
class MyList:
    def __init__(self,iterable=()):
        self.data=list(iterable)


    # def __add__(self,other):
    #     print('__add__被调用')
    #     v=self.data+other.data
    #     return MyList(v)

    # def __mul__(self,other):
    #     print('__mul__被调用')

    #     v=self.data*other
    #     return MyList(v)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    # def __rmul__(self,lhs):
    #     print('__rmul__被调用')
    #     return MyList(self.data*lhs)

    # def __iadd__(self,rhs):
    #     print('__iadd__方法被调')
    #     self.data+=rhs.data
    #     return self
#     def __neg__(self):
#         G=[-x for x in self.data]
#         return MyList(G)

#     def __invert__(self):
#         return self.data[::-1]


# L1=MyList([1,-2,3,-4,5])
# L2=-L1
# L2=~L1
# print(L2)



# 二元运算符


# class MyList:
#     def __init__(self,iterable=()):
#         self.data=list(iterable)

#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     # def __contains__(self,e):
#     #     # if e in self.data:
#     #     #     return True
#     #     # else:
#     #     #     return False
#     #     # return e in self.data
#     #     return e if e in self.data else False


# L1=MyList([1,-2,3,-4,5])
# if 2 in L1:#等同于if L1.__contains__(2):
#     print('2在L1内')
# else:
#     print('不在')


# if 4 not in L1:# if not L1.__contains__(4)
#     print('4不在')
# else:
#     print('4在')


# x=L1[3]#L1和３去运算
# print(x)
#TypeError: 'MyList' object does not support indexing


# 索引切片


# class MyList:
#     def __init__(self,iterable=()):
#         self.__data=list(iterable)

#     def __repr__(self):
#         return 'MyList(%s)' % self.__data

#     def __getitem__(self,i):
#         if type(i) is int:
#             print('用户正在用索引取值')
#         elif type(i) is slice:
#             print('用户正在用切片取值')
#             print('切片起点',i.start)#i即是slice的一个对象　访问对象属性
#             print('切片终点',i.stop)
#             print('步长',i.step)
#         elif type(i) is str:
#             print('正在用字符串')

#         return self.__data[i]      

#     def __setitem__(self,i,v):
#         '''此方法可以让自定义的列表支持索引赋值操作'''
#         # print('__setitem__被调用')
#         self.__data[i] = v
#     def __delitem__(self,i):
#         del self.__data[i]
#         self.__data.pop(i)




# L1=MyList([1,-2,3,-4,5])
# print(L1)
# x=L1[3]
# print(x)

# L1[3]=400#L1.__setitem__(3,400)
# print(L1)

# del L1[3]
# print(L1)

# L1[3]=400
# print(L1)


#思考如下语句
# print(L1[::2])#切片取值
# L1[slice(0,0,2)]




# 特性属性：　@property

class Student:
    def __init__(self,s):
        self.__score=s

    def setscore(self,s):
        '''此方法用设置值加以限制以保证数据的准确性'''
        if 0 <= s <= 100:
            self.__score=s

    @property
    def score(self):
        '''gettter只用来获取数据'''
        print('getter被调用')
        return self.__score




s=Student(50)
s.setscore(100)
score=s.score#访问特性属性实质是调用s.score()
print('成绩是',score)