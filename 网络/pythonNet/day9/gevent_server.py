import gevent 

from gevent import monkey 

#
monkey.patch_all()

from socket import *
from time import ctime

def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',port))
    s.listen(3)
    while True:
        c,addr=s.accept()
        print('connect from ',addr)
        # handler(c)#这时候是只能连接一个客户端
        gevent.spawn(handler,c)#生成协程对象　，产生协程空间　回到上层循环，收到新的客户端连接　产生新的协程空间　


def handler(c):
    while True:
        data = c.recv(1024)#协程都阻塞在recv里面，哪个能运行就运行一遍　
        if not data:
            break
        print(data.decode())

        c.send(ctime().encode())

    c.close()




if __name__ == '__main__':
    server(8888)