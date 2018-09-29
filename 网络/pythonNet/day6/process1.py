#! /usr/bin/env python3 

from multiprocessing import Process
from time import sleep 

#带参数的进程函数　
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print('I am {}'.format(name))
        print('I am working')

p=Process(target = worker,args=(2,'zhang'))

p.start()
#进程名称
print('Process name',p.name)
#获取进程pid号
print('Process PID',p.pid)

p.join(3)
print('===================')



