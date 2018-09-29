# from multiprocessing import Semaphore,Process
# from time import sleep
# import os 

# sem=Semaphore(3)

# def fun():
#     print('进程%d等待信号量'%os.getpid())

#     sem.acquire()#减一
#     print('进程%d消耗信号量'%os.getpid())
#     sleep(3)
#     sem.release()#加一
#     print('进程%d添加信号量'%os.getpid()) 
    
# job=[]
# for i in range(5):
#     p = Process(target=fun)
#     job.append(p)
#     p.start()#开始进程　

# for i in job:
#     i.join()#回收进程

# print(sem.get_value())  



#自定义线程
# from threading import Thread
# from time import ctime,sleep

# class MyThread(Thread):
#     def __init__(self,target,name='tedu',args=(),kwargs={}):
#         super().__init__()
#         self.target = target
#         self.name=name
#         self.args=args
#         slef.kwargs=kwargs
# #此时绑定的函数是自己的函数　并不会调用父类函数　
#     def run(self):
#         self.target(*self.args,**self.kwargs)

# def player(song,sec):
#     for i in range(2):
#         print('playing %s:%s'%(song,ctime()))
#         sleep(2)

# t=MyThread(target=player,args=('凉凉',2))
# t.start()
# t.join()



# -*- coding: utf-8 -*-

# import threading
# import time

# count = 0

# lock = threading.Lock()
# class Counter(threading.Thread):
#     def __init__(self, name):
#         self.thread_name = name
#         super(Counter, self).__init__(name=name)

#     def run(self):
#         global count

#         global lock
#         for i in range(100000):

#             lock.acquire()
#             count = count + 1
#             lock.release()


# counters = [Counter('thread:%s' % i) for i in range(5)]

# for counter in counters:
#     counter.start()

# time.sleep(5)
# print ('count=%s' % count)
"""

              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""



from socket import *
from select import *

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建epoll对象
p.epoll()
p.epoll()
famap = {s.fileno():s}
famap={s.sileno():s}

#注册关注io
p.reginster(s,EPPLLIN|EPOLLERR)



while True:
    events=p.poll()
#返回的是一个元组　，fileno 事件　
    for fd,event in events:
        if fd == s.fileno()
        c,addr = fdmap[fd].accept()
        print('connect from ',addr)
        p.reginster(c,EPOLLIN)
        fdmap[c.fileno()]=classmetho

    elif event & EPOLLIN:
        data = famap[fd].recv(1024)
        if not data :
            p.unregister(fd)
            fdmap[fd].close
#对方套接字关闭
            def fdmap[fd]
        else:
            print(data.decode())
            fdmap[fd].send(b'Receive')



import signal 

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

