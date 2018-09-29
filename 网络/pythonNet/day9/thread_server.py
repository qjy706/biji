from socket import *
import os,sys
from threading import *
import traceback 
import signal 

HOST=''
PORT=8888
ADDR=(HOST,PORT)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

def handler(connfd):
    print("Connect from",connfd.getpeername())
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.send(b'Receive your msg')
    connfd.close()
#进程加　sys.exit(0)




while True:
    try:
        connfd,addr=s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except Exception:
        traceback.print_exc()#打印异常详细信息
        continue
#考虑一个函数设计时候，考虑功能　参数　返回值　参数返回值依据功能
    t=Thread(target = handler,args=(connfd,))#线程是全局变量　但是有下一个客户端进来时候　这个套接字被重新赋值　如果都用全局变量，那么所有线程都在操作最新连接的客户端，所以必须要传参　用局部变量　
#变成Process　则不需要args 进程是独立的　创建的connfd也是不一样的

#join是阻塞函数　，主线程运行到这里阻塞　要等待子线程运行　 为了不阻塞　变成守护子线程
    t.setDaemon(True)
#进程是　Daemon=True    
    t.start()


    # t=Thread(target=fun,args=)



 

