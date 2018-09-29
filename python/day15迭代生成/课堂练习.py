# L=[1,3,5,7]
# it=iter(L)  #让Ｌ提供一个能访问自己的迭代器
# next(it)   # 1从迭代器中取值，让迭代器去获取Ｌ中的一个元素
# L=[2,3,5,7]
# it=iter(L)
# while True:
#     try:
#         x=next(it)
#         print(x)
#     except:
#         break 
# L=[2,3,5,7]
# it=iter(L)
# try:
#     while True:
#         x=next(it)
#         print(x)
# except:
#     pass





# 有一个集合　s={'唐僧','悟空','八戒','沙僧'}
# 用for语句来遍历所有元素如下
# for x in s:
#     print(x)
# else:
#     print('遍历结束')
# 该写成while语句和迭代器


# s={'唐僧','悟空','八戒','沙僧'}
# it=iter(s)
# try:
#     while True:
#         a=next(it)
#         print(a)
# except:
#     print('遍历结束')

# # while True:
# #     try:
# #         a=next(it)
# #         print(a)
# #     except:
# #         break
# # print('遍历结束')


#生成器函数

# def myyield():
#     print('即将生成２')
#     yield 2# 生成器表达式
#     print('即将生成3')
#     yield 3
#     print('即将生成5')
#     yield 5
#     print('即将生成7')
#     yield 7
#     print('生成器生成结束')
# print(myyield())
# <generator object myyield at 0x7fe2f29dfeb8>
# 调用函数的时候，没有打印　，因为根本没有执行　是一个生成器函数　
# 生成器作用有点像　range函数，　返回的一定是可迭代对象　

# for x in myyield():　　＃　myyield是可迭代对象
#     print(x)
# 2
# 3
# 5
# 7
# 生成器生成结束

# gen=myyield() # 绑定这个函数对象　
# it=iter(gen)   #迭代器用变量绑定　
# while True:
#     try:
#         a=next(it)
#         print(a)
#     except:
#         break
# print(next(it))# 此时生成器函数才开始执行，并遇到yield停止
# print(next(it))
# print(next(it))


# 练习　
# 写一个生成器函数，　myeven(start,stop),用来生成，start开始到stop结束的偶数

# def myeven(start,stop):
#     while start < stop:
#         if start % 2 == 0:
#             yield start
#         start += 1
# for x in myeven(1,10):
#     print(x)
# 生成器都是可迭代对象　


# 写一个生成器函数，myfactorial(n)此函数用来生成n个从1开始的阶乘


# def myfactorial(n):
#     i=1
#     for x in range(1,n+1):
#         i *= x
#         yield i

# for x in myfactorial(5):
#     print(x)

# 列表推导式
# gen=(x**2 for x in range(1,5))
# it=iter(gen)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 已知有一个列表　L=[2,3,5,7]
# 1,写一个生成器函数，让此函数能够动态提供数据，数据为原列表
# 的数字的平方加１
# ２，写一个生成器函数，让此函数能够动态提供数据，数据为原列表的数字的平凡
# 加１
# ３，生成一个列表，此列表内的数据是原列表数据的平方加１
# L=[2,3,5,7]
# newL=((x**2+1 for x in L))
# it=iter(newL)
# try:
#     while True:
#         print(next(it))
# except:
#     pass


# def myyield():
#     L=[2,3,5,7]
#     for x in L:
#         yield x**2+1　　# 生成器函数（表达式）生成的是一个可迭代对象　
# 想要取值要用遍历for或者iter() next(iter())获取　
# 一个生成器是一次性的　，一次遍历取完之后第二次就不能取出来了　
# for i in myyield():
#     print(i)


# L=[2,3,5,7]
# L2=[x**2+1 for x in L]  #列表已经定死　不会因为Ｌ变化而变化了
# it= iter(L2)
# print(next(it))
# L[1]=30
# print(next(it))

# # 生成器表达式
# L=[2,3,5,7]
# gen=(x**2+1 for x in L)
# it= iter(gen)
# print(next(it))    #动态的　next会向gen里面的L数据，Ｌ改变了数据也会改变
# L[1]=30
# print(next(it))   # 生成器推导式是现用现生成　，里面不储存任何数据，
# 列表推导式是一次性生成静态数据

#zip

# def myzip(iter1,iter2):
#     it1=iter(iter1)  # 用iter函数去绑定可迭代对象iter1
#     it2=iter(iter2)
#     while True:
#         try:
#             t=(next(it1),next(it2))
#             yield t
#         except:
#             break

# numbers = [10086,10000,10010,95588]
# names=['中国移动','中国电信','中国联通']
# for t in myzip(numbers,names):
#     print(t)


# 写一个程序　，读入任意行文字，当输入空行时结束输入
# 打印带有行号的输入结果
# 请输入abcde
# 请输入hello
# 请输入bye
# 请输入 回车　
# 输入如下　
# 第一行：abcde
# 2 hello
# 第三行bye


# def myfun():
#     L=[]
#     s=1
#     while s <= 3:
#         a=input('请输入任意文字')   #if not a
#         b=input('')
#         L.append(a)            
#         s+=1
#     for x in enumerate(L):
#         print('第%d行: %s ' % x)
# myfun()




# numbers=23
# guess= int(input('输入一个整数'))
# if guess == numbers:
#     print('恭喜你猜对了')
#     print('but you do not win any prizes!')
# elif guess < numbers:
#     print('no,it is a little higher than that')
# else:
#     print('no,it is a little lower than that')
# print('done')







# L=[x for x in prime(10,20)]    # L=[11,12,17,19]


# 写一个生成器函数myxrange([start,],stop[,step])
# 来生成一系列函数　
# 要求　myxrange功能与range功能相同（不允许调用range函数）
# 用自己写的myxrange函数结合生成器表达式求1-10内奇数的平方和

# 思考　
# 学生信息管理系统每次ｕ启动时都要重新输入数据
# 如何让学生管理系统启动时就自动家在以前输入过的数据
# （预习　文件操作）


# def sushu(n):
#     L=[]
#     for i in range(n):
#         if i < 2:
#             pass
#         for x in range(2,i):
#             if i % x != 0:
#                 L.append(i)
#     return L
# print(sushu(10))



# 今日作业　用生成器函数，生成素书，给出起始值begin和终止值end 
# 生成begin 到end范围内的素数
# 如　

# def myfun(n):
#     if n < 2:
#         pass
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#         return n
# def prime(begin,end):
#     for x in range(begin,end):
#         if myfun(x):
#             yield x
# for i in prime(10,20):
#     print(i)









# 写一个生成器函数myxrange([start,],stop[,step])
# 来生成一系列函数　
# 要求　myxrange功能与range功能相同（不允许调用range函数）
# 用自己写的myxrange函数结合生成器表达式求1-10内奇数的平方和

# def myxrange(start=0,stop=0,step=1):
#     x=start
#     while x <= stop-1:
#         yield x
#         x += step
# for x in myxrange(10,20):
#     print(x)

# gen=(x**2 for x in myxrange(1,10) if x % 2 == 1)
# L=[]
# for i in gen:
#     L.append(i)
# print(sum(L))




# L=[2,3,5,6]
# for x in L:
#     print(x)

# it=iter(L)
# while True:
#     try:
#         x=next(it)
#         print(x)
#     except:
#         break

# def myyield():
#     yield 1
#     yield 2
#     yield 3
#     return 6
#     yield 4
# a=myyield()
# it=iter(a)
# while True:
#     try:
#         a=next(it)
#         print(a)
#     except:
#         break

# numbers = [10086,10000,10010,95588]
# names=['中国移动','中国电信','中国联通']
# for t in zip(numbers,names):
#     print(t)



# for No,numbers,names in zip(range(1,100),numbers,names):
#     print(No,numbers,names) #zip是根据可迭代对象参数形成一个元组

# names=['中国移动','中国电信','中国联通']
# for t in enumerate(names):
#     print(t) 


it=iter(range(8,20))
print(next(it))
print(next(it))

print(next(it))

print(next(it))

print(next(it))
numbers = [10086,10000,10010,95588]
names=['中国移动','中国电信','中国联通']
for t in zip(numbers,names):
    print(t)

for No,numbers,names in zip(range(1,100),numbers,names):      
    print(No,numbers,names) 