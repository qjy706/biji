from socket import *

# s= socket()

# s_addr=('0.0.0.0',10000)

# s.bind(s_addr)

# while True:
#     data.addr = s.recvfrom(4096)
#     if not data:
#         break
#     print('connect from ',addr)
#     print(data.decode())

#     s.sendto('已收到消息'.encode(),addr)

# s.close


#阻塞io input recn accept join 

# from time import ctime,sleep
# s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('0.0.0.0',10000))
# s.listen(5)
# # s.setblocking(False)
# s.settimeout(5)

# while True:
#     try:
#         c,addr=s.accept()
#     except:
#         sleep(1)
#         print(ctime())
#         continue

# from select import select
# from socket import *
# #select模块中的select方法
# s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('0.0.0.0',8888))
# s.listen(5)
# s.setblocking(False)
# print(s.fileno())

# rlist=[s]
# wlist=[]
# xlist=[]

# while True:
#     rs,ws,xs=select(rlist,wlist,xlist)
#     for r in rs:
#         if r == s:
#             c,addr = r.accept
#             rlist.append(c)
#         else:
#             data=r.recv(1024)
#             if not data:
#                 rlist.remove(r)
#                 r.close() 
#             else:
#                 print(data.decode())
#                 #讲客户端套接字放入wlist列表
#                 # wlist.append(r)
#                 r.send(b'Receive your message')



from socket import *
from select import *
import sys,os 
from threading import Thread

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',10000))
s.listen(6)
#创建poll对象　
p=poll()
#唯一正整数绑定的套接字
fdmap={s.fileno():s}

#注册关注io  select rlist wlist xlist
p.register(s,POLLIN|POLLERR)
while True:
    events=p.poll()#监控时间发生
    #event里面时fileno event
    for fd,event in events:
        if fd == s.fileno():
            c,addr=fdmap[fd].accept()
            p.register(c,POLLIN)
            fdmap[c.fileno()]=c
        elif event & POLLIN:
            data=fdmap[fd].recv(1024)
            if not data:
                #从关注时间中移除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]

            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')



s = socket()
HOST=''
port=8000
ADDR=(HOST,port)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

c,addr=s.accept()

t=Thread(target = handler,args=(c,))
t.setDaemon(True)
t.start()


