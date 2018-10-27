from socket import *
import os 

#先确定套接字　文件　
sock_file='./sock_file'

#判断文件是否存在　
if os.path.exists(sock_file):
    os.remove(sock_file)

#创建本地套接字　
sockfd=socket(AF_UNIX,SOCK_STREAM)


sockfd.bind(sock_file)

#监听
sockfd.listen(5)

#消息接收　
while True:
    c,addr=sockfd.accept()
    while True:
        data=c.recv(1024)
        if data:
            print(data.decode())
            c.send(b'Receive')
        else:
            break
    c.close()
sockfd.close()


from socket import *
import os 

kobe='./kobe'

if os.path.exists(kobe):
    os.remove(kobe)

s=socket(AF_UNIX,SOCK_STREAM)

s.bind(kobe)

s.listen(5)

while True:
    c,addr=s.accept()
    while True:

        data=c.recv(1024)
        if data:
            print(data.decode())
        else:
            break

        c.send(b'666')
    c.close()
s.close()




if os.path.exists(james):
    os.remove(james)

if os.path.exists(james):
    os.remove(james)

if os.path.exists(james):
    os.remove(james)

if os.path.exists(james):
    os.remove


import os
import time 

a=1

pid = os.fork()

if pid < 0:
    print('666')

elif pid == 0:
    s=0
    while s < 10:
        a += 1
        s += 1  
    print(a,s)
else:
    time.sleep(2)
    a += 1
    print(a)
