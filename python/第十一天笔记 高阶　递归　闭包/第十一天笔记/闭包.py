# 写一个函数创建x的y次方的函数　
# def make_power(y):
#     def fn(x):        # 有一个内嵌函数
#         return x ** y    # fn是一个闭包 y是外部函数变量　
#     return fn　　　　# 返回了内嵌函数　fn
# pow2=make_power(2) #外部函数提前设号参数
# print('5的平方是:',pow2(5))  # 5其实带入了x

#pow2其实绑定的是函数内部嵌套函数fn  fn创建了一个空间 
# pow2(5)传参给了fn(x)

#2 
#用闭包创建任意的函数
# f(x)=ax2+bx+c

# def get_fx(a,b,c):
#     def fx(x):
#         return a*x**2+b*x+c
#     return fx
# print


# 已知有五位朋友在一起
# 第五个人说他比第四个人大两岁
# 第四个人说他比第三个人大两岁　
# 第三个人说他比第二个人大两岁
# 第二个人说他比第一个人大两岁
# 第一个人说它10岁
# 编写程序　
# 第五个人几岁
# 第三个人几岁

# def age(n):
#     if n == 1:
#         return 10
#     return age(n-1)+2



# print(age(5))



# L=[[13,5,8],10,[[13,14],15,18],20]
# 写一个函数print_list(lst) 打印出所有的数字

def print_list(lst):
    l=[]
    for x in lst:
        if type(x) is list:
            print_list(x)
        l.append(x)
    return l
L=[[13,5,8],10,[[13,14],15,18],20]
print(print_list(L))
