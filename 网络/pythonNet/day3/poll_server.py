from socket import *
from select import *

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
print(s)
#创建poll对象　
p=poll()

#fileno ---->  IO对象字典
fdmap={s.fileno():s}
print(fdmap)


#注册关注io
p.register(s,POLLIN|POLLERR)

while True:
    #进行IO监控　 准备就绪以元祖形式返回列表　元祖有两项
    events=p.poll()
    #event返回的是一个列表　里面的元素是元组　
    #[(fileno event)]
    print(events)
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('connect from',addr)
            #添加新的关注事件
            p.register(c,POLLIN)

            fdmap[c.fileno()] = c

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





