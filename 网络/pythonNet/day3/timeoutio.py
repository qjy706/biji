#超时

from socket import *

from time import sleep,ctime 

s=socket()
s.bind(('127.0.0.1',8888))
s.listen(5)


#将套接字设置为超时时间
s.settimeout(5)


while True:
    print('waiting for connect')
    try:
        c,addr=s.accept()
    except timeout:
        sleep(2)
        print(ctime())
        continue
    else:
        print('connect from',addr)
        while True:
            data=c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()

s.close()