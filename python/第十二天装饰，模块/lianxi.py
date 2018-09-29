# 装上装饰器后，装饰器函数被调用　装饰器函数的
# 实参是被装饰的函数，被装饰函数带入装饰器函数　

# import time 
# year=int(input('请输入年份'))
# month=int(input('请输入月份'))
# day=int(input('请输入天数'))
# times=time.time()
# print(times)
# both_time=time.mktime((year,month,day,0,0,0,0,0,0))
# print(both_time)
# a=time.asctime((year,month,day,0,0,0,0,0,0))
# print(a)
# s=times-both_time
# print(s)
# l=time.localtime(s)

# print(l)

import time
while True:
    l=time.localtime()
    s=time.asctime(l)
    L=s.split(' ')
    print(L[3])
    time.sleep(1)