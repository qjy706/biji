from socket import *
import os,sys
import signal#处理子进程退出　产生的僵尸进程的大量积累　　wait的话会阻塞　

#创建套接字　
HOST=''#不写跟0.0.0.0一样　
PORT=8888
ADDR=(HOST,PORT)

s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

print('进程%d等待客户端连接'%os.getpid())

#在父进程中忽略子进程状态改变,子进程退出自动由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def client_handler(c):
    print('处理子进程请求',c.getpeername())
    try:
        while True:
            data = c.recv(1024)
            if not data:
                break
            print(data.decode())
            c.send('收到请求'.encode())
    except (KeyboardInterrupt,SystemError):
        sys.exit('客户端推出')
    except Exception as e:
        print(e)
    c.close()
    sys.exit(0)#让子进程退出，这样这样不会影响到s套接字


while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print('Error:',e)
        continue

    #有客户端链接进来　为客户端创建新的进程处理请求　
    pid = os.fork()
#子进程处理具体的请求　
    if pid == 0:
        s.close()
        client_handler(c)


#不管是创建失败还是父进程运行　都要回到上层循环　继续等待下个客户端连接
    else:
        c.close()
        continue




