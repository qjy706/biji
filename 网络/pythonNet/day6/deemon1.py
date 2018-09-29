#! /usr/bin/env python3 

from multiprocessing import Process
from time import sleep,ctime

def tm():
    while True:
        sleep(2)
        print(ctime())

p=Process(target = tm)
p.daemon = True#必须在子进程开始运行之前使用　并且与join最好不要一起使
p.start()
sleep(5)
print('main process exit')

#主进程五秒结束　但是子进程并没有结束
#加上p.daemon