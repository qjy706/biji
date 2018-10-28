from socket import *
from select import *
from time import ctime,sleep
import sys
import os 
from threading import Thread
from multiprocessing import Process


#tcp
# s=socket()
# ADDR=('0.0.0.0',8000)
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(ADDR)
# s.listen(5)
# while True:
#     c,addr = s.accept()

#udp
s=socket(AF_INET,SOCK_DGRAM)
# 设置套接字可以发送接受广播　
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
ADDR=('0.0.0.0',8000)
s.bind(ADDR)
while True:
    data,addr = s.recvfrom(buffersize)
    if not data:
        break 
    print('from {}:{}'.format(addr,data.decode()))
    s.sendto(b'ok',addr)
s.close()



#io多路复用

s=socket()
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
s.setblocking(False)
print(s.fileno())

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    print('有io事件发生')
    for r in rs:
        if r == s:
            c,addr = s.accept()
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                r.close()
                rlist.remove(c)
            else:
                print(data.decode())
                r.send(b'receive your message')


#epoll | poll

s=socket()
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

p=poll()

fdmap={s.fileno():s}

# POLLIN  　POLLOUT 　POLLERR　　POLLHUP 　　　　POLLNVAL 
# rlist    　wlist　   xlist    　断开　　　　　　　无效数据

p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()

    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            fdmap[c.fileno()]=c
            p.register(c,POLLIN)

        elif event & POLLIN:
            data = famap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
        else:
            print(data.decode())
            fdmap[fd].send(b'Receive')

#epoll

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(5)
#创建epoll对象　添加注册事件
p=epoll()
p.register(s,EPOLLERR|EPOLLIN)
fdmap={s.fileno():s}

while True:
    events = p.poll()
    for fd,event in events:
        if fd = s.fileno():
            c,addr = fdmap[fd]
            p.register(c,EPOLLIN)
            fdmap[c.fileno()]=c
        elif event & EPOLLIN:
            data=famap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                def fdmap[fd]

            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')

#创建epoll poll对象　注册时间　register() poll方法用列表存储套接字　epoll用字典　
#整型文件描述符和套接字组成字典　　开始阻塞等待io事件发生，　　
#rs,ws,xs = select(rlist,wlist,xlist)
#event=p.poll() 返回的是一个列表　里面是元组　
#便利之后　如果　fd=s.fileno() 则有新的套接字进来，需要注册新的　p.register(c,POLLIN)
#字典添加键值对


rs,ws,xs = select(rlist,wlist,xlist)
for r in rs:
    pass


p=poll()
p=epoll()

p.register(s,POLLIN|POLLERR)
fdmap={s.fileno():s}

evnets = p.poll()
for fd,event in events:
    if fd == s.fileno():
        c,addr = fdmap[fd].accept()
        fdmap[c.fileno()]=c
        p.register(c,POLLIN)
    elif event & POLLIN:
        data=famap[fd].recv(1024)
        if not data:
            p.unregister(fd)
            fdmap[fd].close()
            def fdmap[fd]

        else:
            print(data.decode())
            fdmap[fd].send(b'Receive')




import os 
from multiprocessing import Process

filename='./xxx'

size = os.path.getsize(filename)

def copy1():
    f = open(filename,'rb')
    n = size // 2

    fw = open('file1.png','wb')
    while True:
        if n < 1024:
            fw.write(n)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    fw.close()
    f.close()

def copy2():
    