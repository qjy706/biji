# def power2(x):
#     return x**2
# for x in map(power2,range(1,10)):
#     print(x)


# s=0 
# for x in map(lambda x:x**2,range(1,10)):
#     s += x
# print(s) 
# 返回一个可迭代的对象，此刻迭代
# 对象用函数func对可迭代对象的每一个元素作为参数计算后得到新的数据
# filter
# 筛选　
# 筛选可迭代对象中的数据，返回一个可迭代对象 for
# 此可迭代对象值每个数据进行布尔值，如果True则保留，返回False
# 则丢弃
# filter 筛选！！！！


# def isodd(x):
#     return x % 2 == 1
# for x in filter(isodd,range(10)):
#     print(x)

# sorted(iterable,key=None,reverse=False)
# key是排序的依据！！
# l=[5,-2,3,4,6]
# L=sorted(l,key=abs)
# print(L)   key 可以是内建函数，也可以是一个函数

# def jiecheng(n):
#     if n == 1:
#         return 1
#     return n*jiecheng(n-1)
#     print(jiecheng(10))



# 已知有五位朋友在一起
# 第五个人说他比第四个人大两岁
# 第四个人说他比第三个人大两岁　
# 第三个人说他比第二个人大两岁
# 第二个人说他比第一个人大两岁
# 第一个人说它10岁
# 编写程序　
# 第五个人几岁
# 第三个人几岁
#门一扇扇推开但不拿走东西　之后再回来拿东西
# def age(n):
#     if n == 1:
#         return 10
#     return age(n-1)+2　　　　

# print(age(5))   
# L=[[13,5,8],10,[[13,14],15,18],20]
# 写一个函数print_list(lst) 打印出所有的数字
# l=[]
# def print_list(lst):
#     for x in lst:
#         if type(x) is list:
#             print_list(x)
#         else:
#             l.append(x)
#     return l
# L=[[13,5,8],10,[[13,14],15,18],20]
# print(print_list(L))     

# 写一个函数sum_list(lst) 返回个列表中所有数字的和

l=[]

def sum_list(lst):
    s=0
    for x in lst:
        if type(x) is list:
            s += sum_list(x)
        else:
             s += x
    return s



L=[[13,5,8],10,[[13,14],15,18],20]
print(sum_list(L))