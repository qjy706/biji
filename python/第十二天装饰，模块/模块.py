# import math  # 导入数学模块
# # print(math.cos(0))
# # print(math.sin(0))   #sin是属性　　模块名.属性名
# r=int(input('请输入一个圆的半径'))
# s=math.pi*r**2
# print(s)

# import math as m   # 给模块起了一个别名
# s=int(input('请输入一个圆的面积'))
# r=s/(m.pi)
# print(m.sqrt(r))


# from math import sin as fac
# print(fac(5))

# from math import *
# print(sin(pi/2))


# import math
# math.sin(5)
# print(math.sin(5))  

# from math import sin as s
# print(s(5))

# from math import *
# print(factorial(10))
# print('程序开始')
# import time
# time.sleep(10)
# print('结束')


# 写一个程序，输入你的出生日期
# １）　算出你已经出生了多少天
# ２）算出你出生那天是星期几
# year=int(input('年份'))
# month=int(input('月份'))
# day=int(input('天数'))
# import time
# s=time.time()
# p=time.mktime((year,month,day,0,0,0,0,0,0))
# b=s-p
# days=b//3600//24
# print('出生了',days,'天')

# t=time.localtime(p)
# week={0:'星期一',1:'星期二',2:'星期三',
# 3:'星期四',4:'星期五',５:'星期六',6:'星期天'}
# print('出生那天是星期',week[t[6]])



