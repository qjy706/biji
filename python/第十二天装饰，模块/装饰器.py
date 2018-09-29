
#while True 无线循环 

# def mydeco(fn):       #装饰器函数
#     def fx():
#         print('fx被调用')
#         fn()　　　# 调用被装饰函数
#         print('被装饰函数调用之后')
#     return fx

# @mydeco
# def myfun():
#     print('myfun被调用')   # myfun=mydeco(myfun)

# myfun()
# myfun()
# myfun()
# 等于在原有函数myfun基础上加了mydeco　　因为mydeco(myfun)
# 会把函数　myfun作为参数带入了mydeco
# 实质就是替换一个变量名 把myfun的函数变成里mydeco(myfun)

# def privileged_check(fn):
#     print('aaaaaa')
#     def fx(name,x):
#         print('正在进行权限验证...')
#         if True:
#             fn(name,x)
#         else:
#             print('权限验证失败')
#     return fx

# def message_send(fn):
#     def fy(n,money):
#         fn(n,money)
#         print('正在发送短信',n,)
#     return fy

# @message_send
# @privileged_check
# def savemoney(name,x):
#     print(name,'存钱',x,'元')  
# # 实质：
# #savemoney=privileged_check(savemoney) 离得最近
# # savemoney=message_send(savemoney) 2 
# # 一层套一层　　fx 带进去fy
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
# savemoney(123,400)

# aaaaaa
# 正在进行权限验证...
# 123 存钱 400 元
# 正在发送短信 123


# 参数直接带进去闭包





# s=0
# def sum(x):
#     global s
#     for i in range(1,x+1):
#         s += i**2
#     return s
# print(sum(100))


L=[1,2,3]
def f(n=0,lst=[]):　
# 在缺省参数［］在def语句执行时创建此列表
#并一直被ｆ函数绑定
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)

#　lst=[] 
# 列表是可变的，
# 列表不是每次调用都创建缺省参数
# 在ｄｅｆ语句创建是就已经创建好，记录以前的结果









