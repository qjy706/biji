# 多线程并发
# from socket import *
# import os,sys
# from threading import *
# import traceback 
# import signal 

# while True:
#     try:
#         connfd,addr = s.accept()
#     except KeyboardInterrupt:
#         s.close()
#         sys.exit('服务器退出')
#     except Exception:
#         traceback.print_exc()#打印更详细信息
#         continue#返回循环

#     t=Thread(target = handler,args=(connfd,))

#     t.setDaemon(True)#父线程退出子线程退出
#     t.start()

# def handler(conngfd):
#     while True:
#         data = connfd.recv(1024).decode()
#         if not data:
#             break
#         print(data)
#         connfd.send(b'Receive your msg')
#     connfd.close()


# from socket import *
# from threading import *
# import sys

# HOST='0.0.0.0'
# PORT=8000
# ADDR=(HOST,PORT)
# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(ADDR)
# s.listen(5)

# while True:
#     try:
#         c,addr = s.accept()
#     except KeyboardInterrupt:
#         s.close()
#         sys.exit('服务器退出')
#     except Exception:
#         traceback.print_exc()#打印更详细信息
#         continue#返回循环
#     t = Thread(target = handler,args=(c,))
#     t.setDaemon(True)
#     t.start()
# s.close()

# def handler(c):
#     while True:
#         data = c.recv(1024)
#         if not data:
#             break
#         print(data.decode())
#         c.send(b'666')
#     c.close()
#     



from socket import *
import os,sys 
import signal 
import traceback

HOST=''#不写跟0.0.0.0一样　
PORT=8888
ADDR=(HOST,PORT)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except:
        traceback.print_exc()
        continue
    pid = os.fork()
    if pid == 0:
        s.close()
        handler(c)#在子进程进行操作 子进程要及时退出
    else:
        c.close()
        continue

#接收套接字与客户端收发分开　进行多进程操作　

def handler(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.encode())
        c.send(b'ok')
    c.close()
    sys.exit(0)





