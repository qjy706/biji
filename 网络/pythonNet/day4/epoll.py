from socket import *
from select import *

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象　

p.epoll()

#fileno ---->  IO对象字典
fdmap={s.fileno():s}



#注册关注io
p.reginster(s,EPOLLIN|EPOLLERR)

while True:
    #进行IO监控　 准备就绪以元祖形式返回列表　元祖有两项
    events=p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('connect from',addr)
            #添加新的关注事件
            p.reginster(c,EPOLLIN)

            fdmap[c.fileno()] = c

        elif event & EPOLLIN:
            data=famap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                def fdmap[fd]

            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')