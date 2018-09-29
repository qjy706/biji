#创建二级子进程避免僵尸　
#成为孤儿就不会成为僵尸
import os 
from time import sleep
import sys

def f1():
    sleep(3)
    print('第一件事')

def f2():
    sleep(4)
    print('第二件事')


pid = os.fork()

if pid < 0:
    print('error')

elif pid == 0:
    #创建二级子进程
    p = os.fork()
    if p == 0:
        f2()

    else:
        os._exit()
        # sys.exit()



else:
    os.wait()#等待一级子进程退出
    f1()


#相当于多进程了
