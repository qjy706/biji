from socket import *

q=socket(AF_INET,SOCK_STREAM)
#创建套接字
q.connect(('127.0.0.1',10000))
#连接端口　ip 

while True:
    data=input('发送 ')
    q.send(data.encode())
    if data == '##':
        break

    data=q.recv(4096)
    print(data.decode())

q.close()



from socket import *

class socket:
    def __init__(self,a=AF_INET,b=SOCK_STREAM):
        self.a=AF_INET
        self.b=SOCK_STREAM

    def socket(self):
        self.c=self.socket(self.a,self.b)

    def bind(self,L=(a,b)):
        self.c.bind(L)

    def listen(self,n):
        self.c.listen(n)


    def accept(self):
        self.fd,self.addr=self.c.accept()


    def sendandrecv(self,n,L=()):
        self.socket()
        self.bind(L)
        self.listen(n)
        self.accept()
        while True:
            data=self.fd.recv(4096).decode()
            if data == '##':
                break
            print(data)
            data=self.fd.send(b'666')
        self.fd.close()
        self.c.close()


